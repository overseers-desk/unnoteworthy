#!/usr/bin/env wish9.0
# A markdown file viewer: one document of foldable sections, one per
# heading, rendered through tkdown into a streamdoc text widget.
#
#   wish9.0 viewer.tcl README.md
#
# Click a heading to fold its section; folding a heading also folds the
# deeper headings under it. Fold all gives the table of contents. F5 reloads
# the file from disk, Ctrl-O opens another.

package require Tcl 9
package require Tk

set HERE [file dirname [file normalize [info script]]]
::tcl::tm::path add [file join $HERE modules]
package require streamdoc
package require tkdown

# Reading fonts derived from the Tk defaults, created once per interp. The
# dict is what ::tkdown::tags takes; the heading faces step up from body.
proc ensure_fonts {} {
    if {"SVBody" ni [font names]} {
        set body [font actual TkTextFont]
        set mono [font actual TkFixedFont]
        set size [dict get $body -size]
        font create SVBody           {*}$body
        font create SVBodyBold       {*}$body -weight bold
        font create SVBodyItalic     {*}$body -slant italic
        font create SVBodyBoldItalic {*}$body -weight bold -slant italic
        font create SVMono           {*}$mono
        font create SVH1 {*}$body -weight bold -size [expr {int($size * 1.6)}]
        font create SVH2 {*}$body -weight bold -size [expr {int($size * 1.3)}]
        font create SVH3 {*}$body -weight bold -size [expr {int($size * 1.1)}]
    }
    return [dict create body SVBody bold SVBodyBold italic SVBodyItalic \
        bolditalic SVBodyBoldItalic mono SVMono h1 SVH1 h2 SVH2 h3 SVH3]
}

# Split a markdown file into sections at ATX heading lines that sit outside
# fenced code. Returns a list of {level title body}; the first element is
# the text before any heading, level 0 and no title, and is omitted when
# that text is blank. Bodies keep their fences verbatim for tkdown.
proc split_headings {text} {
    set sections [list]
    set level 0; set title ""; set lines [list]
    set fence ""
    foreach line [split $text \n] {
        if {$fence ne ""} {
            if {[string match "$fence*" [string trimleft $line]]} { set fence "" }
            lappend lines $line
            continue
        }
        if {[regexp {^\s{0,3}(```+|~~~+)} $line -> f]} {
            set fence $f
            lappend lines $line
            continue
        }
        if {[regexp {^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$} $line -> hashes t]} {
            lappend sections [list $level $title [join $lines \n]]
            set level [string length $hashes]; set title $t; set lines [list]
            continue
        }
        lappend lines $line
    }
    lappend sections [list $level $title [join $lines \n]]
    if {[lindex $sections 0 0] == 0 && [string trim [lindex $sections 0 2]] eq ""} {
        set sections [lrange $sections 1 end]
    }
    return $sections
}

oo::class create Viewer {
    superclass ::streamdoc::StreamDoc
    variable Top Text
    variable Host        ;# the frame holding the toolbar and the document
    variable Path        ;# the open file, "" before the first open
    variable MeasureTok  ;# pending idle re-measure, "" when none

    constructor {parent} {
        set Host $parent
        set Path ""
        set MeasureTok ""
        my configure -font SVBody
        ttk::frame $parent.bar
        pack $parent.bar -side top -fill x
        ttk::button $parent.bar.open -text "Open" -command [list [self] open_dialog]
        ttk::button $parent.bar.reload -text "Reload" -command [list [self] reload]
        ttk::button $parent.bar.fold -text "Fold all" -command [list [self] fold_all]
        ttk::button $parent.bar.expand -text "Expand all" -command [list [self] expand_all]
        ttk::label $parent.bar.path -text "" -anchor w
        pack $parent.bar.open $parent.bar.reload -side left -padx 2 -pady 2
        pack $parent.bar.expand $parent.bar.fold -side right -padx 2 -pady 2
        pack $parent.bar.path -side left -fill x -expand 1 -padx 8
        pack [ttk::frame $parent.doc] -fill both -expand 1
        my setup $parent.doc
        ::tkdown::tags $Text [ensure_fonts]
        $Text tag configure body
        $Text tag configure code -font SVMono -background #f3f4f6 \
            -spacing1 2 -spacing3 2
        $Text tag configure hdr -spacing1 10 -spacing3 4
        $Text tag configure h1 -font SVH1
        $Text tag configure h2 -font SVH2
        $Text tag configure h3 -font SVH3
        foreach l {h4 h5 h6} { $Text tag configure $l -font SVBodyBold }
        $Text tag bind hdr <Button-1> [list [self] hdr_click %x %y]
        $Text tag bind hdr <Enter> [list $Text configure -cursor hand2]
        $Text tag bind hdr <Leave> [list $Text configure -cursor {}]
        bind $Text <Configure> [list [self] measure_later]
        set top [winfo toplevel $parent]
        bind $top <F5> [list [self] reload]
        bind $top <Control-o> [list [self] open_dialog]
    }

    # ---- files ----
    method open_file {path} {
        set f [open $path r]
        fconfigure $f -encoding utf-8
        set text [read $f]
        close $f
        set Path $path
        $Host.bar.path configure -text $path
        wm title [winfo toplevel $Top] [file tail $path]
        my render $text
    }
    method reload {} {
        if {$Path eq ""} return
        set view [lindex [$Text yview] 0]
        my open_file $Path
        $Text yview moveto $view
    }
    method open_dialog {} {
        set path [tk_getOpenFile -parent [winfo toplevel $Top] \
            -filetypes {{Markdown {.md .markdown}} {All {*}}}]
        if {$path ne ""} { my open_file $path }
    }

    # ---- rendering ----
    method render {text} {
        my reset
        ::tkdown::forget $Text
        my batch {
            foreach sec [split_headings $text] {
                lassign $sec level title body
                set body [string trim $body \n]
                if {$level == 0} {
                    set m [my append_open]
                    ::tkdown::body $Text $m $body body code
                    my append_close $m
                    continue
                }
                my region_open [dict create level $level title $title]
                set m [my append_open]
                my emit $m "▾ " [list hdr h$level]
                ::tkdown::runs $Text $m $title [list hdr h$level]
                my emit $m "\n" [list hdr h$level]
                if {[string trim $body] ne ""} {
                    ::tkdown::body $Text $m $body body code
                }
                my append_close $m
                my region_close
            }
        }
        my measure
    }

    # ---- folding ----
    method hdr_click {x y} {
        set n [my region_at [$Text index @$x,$y]]
        if {$n < 0} return
        my toggle $n
        if {![my folded $n]} return
        # Folding a heading folds the deeper headings that follow it, so
        # unfolding it later shows them as an outline.
        set level [dict get [my payload $n] level]
        for {set k [expr {$n + 1}]} {$k < [my region_count]} {incr k} {
            if {[dict get [my payload $k] level] <= $level} break
            my fold $k
        }
    }

    # ---- the measure: prose margins follow the pane width ----
    method measure_later {} {
        if {$MeasureTok ne ""} return
        set MeasureTok [after idle [list [self] measure]]
    }
    method measure {} {
        set MeasureTok ""
        set width [winfo width $Text]
        if {$width <= 1} return
        set em [font measure SVBody "0"]
        set margin [expr {max(12, ($width - 2 * [$Text cget -padx] - 90 * $em) / 2)}]
        foreach tag {body hdr} {
            $Text tag configure $tag -lmargin1 $margin -lmargin2 $margin -rmargin $margin
        }
        set inset [expr {$margin + $em}]
        $Text tag configure code -lmargin1 $inset -lmargin2 $inset -rmargin $inset
    }
}

pack [ttk::frame .f] -fill both -expand 1
set viewer [Viewer new .f]
if {[llength $argv]} { $viewer open_file [lindex $argv 0] }
