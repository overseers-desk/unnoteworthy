#!/usr/bin/env wish9.0
# A markdown file viewer: one document of foldable sections, one per
# heading, rendered through tkdown into a streamdoc text widget.
#
#   wish9.0 viewer.tcl README.md
#
# Click a heading to fold its section; folding a heading also folds the
# deeper headings under it. Fold all gives the table of contents. Ctrl-F
# finds text, into folded sections and table cells. Links open: anything
# with a URL scheme in the system browser, a relative .md in this window,
# #anchor by scrolling to the section. F5 reloads the file from disk, Ctrl-O opens another.

package require Tcl 9
package require Tk

set HERE [file dirname [file normalize [info script]]]
::tcl::tm::path add [file join $HERE vendor]
package require streamdoc 1.2
package require tkdown 2.0

# Heading faces step up from tkdown's body face; the rest of the dict is
# the module's own, used only through its keys.
proc viewer_fonts {} {
    set fonts [::tkdown::ensure_fonts]
    set body [dict get $fonts body]
    if {"ViewerH1" ni [font names]} {
        set size [font actual $body -size]
        foreach {name factor} {ViewerH1 1.6 ViewerH2 1.3 ViewerH3 1.1} {
            font create $name {*}[font actual $body] -weight bold \
                -size [expr {int($size * $factor)}]
        }
    }
    return [dict merge $fonts {h1 ViewerH1 h2 ViewerH2 h3 ViewerH3}]
}

# GitHub's anchor for a heading title: inline markup dropped, lower case,
# spaces to hyphens, everything but letters, digits and hyphens removed.
proc heading_slug {title} {
    set plain ""
    foreach run [::tkdown::parse_inline $title] { append plain [lindex $run 1] }
    set s [string tolower [string trim $plain]]
    set s [regsub -all {[^\w\s-]} $s ""]
    return [regsub -all {\s+} $s "-"]
}

oo::class create Viewer {
    superclass ::streamdoc::StreamDoc
    variable Host        ;# the frame holding the toolbar and the document
    variable Doc         ;# the frame the viewer made for streamdoc to build into
    variable Text        ;# the document text widget
    variable Path        ;# the open file, "" before the first open
    variable Anchors     ;# dict: heading slug -> region index
    variable Images      ;# dict: image path -> Tk image, for the open file
    variable Fonts       ;# the fonts dict tkdown paints with
    variable MeasureTok  ;# pending idle re-measure, "" when none

    constructor {parent} {
        set Host $parent
        set Path ""
        set Anchors [dict create]
        set Images [dict create]
        set MeasureTok ""
        set Fonts [viewer_fonts]
        my configure -font [dict get $Fonts body]
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
        set Doc $parent.doc
        my setup $Doc
        set Text [my textwidget]
        # The find bar sits above the text: the document moves to row 1 and
        # place_find takes row 0.
        grid $Text -row 1
        grid $Doc.sb -row 1
        grid rowconfigure $Doc 0 -weight 0
        grid rowconfigure $Doc 1 -weight 1
        ::tkdown::tags $Text $Fonts -quotetags quote \
            -image_cmd [list [self] image_for]
        $Text tag configure code -font [dict get $Fonts mono] -background #f3f4f6 \
            -spacing1 2 -spacing3 2
        $Text tag configure quote -foreground #5a6470
        $Text tag configure hdr -spacing1 10 -spacing3 4
        foreach l {h1 h2 h3} { $Text tag configure $l -font [dict get $Fonts $l] }
        foreach l {h4 h5 h6} { $Text tag configure $l -font [dict get $Fonts bold] }
        $Text tag configure find -background #ffe58a
        $Text tag configure td-link -foreground #1a5fb4 -underline 1
        $Text tag configure td-quotebar -foreground #9aa3ad
        $Text tag configure td-rule -background #d0d4d9
        $Text tag configure td-grid -background #c8ccd2
        $Text tag configure td-spot -background #e5a50a
        $Text tag bind hdr <Button-1> [list [self] hdr_click %x %y]
        $Text tag bind hdr <Enter> [list $Text configure -cursor hand2]
        $Text tag bind hdr <Leave> [list $Text configure -cursor {}]
        $Text tag bind td-link <Button-1> [list [self] link_click %x %y]
        $Text tag bind td-link <Enter> [list $Text configure -cursor hand2]
        $Text tag bind td-link <Leave> [list $Text configure -cursor {}]
        bind $Text <Configure> +[list [self] measure_later]
        set top [winfo toplevel $parent]
        bind $top <F5> [list [self] reload]
        bind $top <Control-o> [list [self] open_dialog]
        bind $top <Control-f> [list [self] find_show]
    }

    # ---- streamdoc hooks ----
    method place_find {frame} {
        grid $frame -in $Doc -row 0 -column 0 -columnspan 2 -sticky ew
    }
    method on_reveal {idx} { ::tkdown::table_spotlight $Text $idx }
    method find_extra {term nocase} {
        concat [::tkdown::table_scan $Text $term $nocase] \
               [::tkdown::link_scan $Text $term $nocase]
    }

    # ---- files ----
    method open_file {path} {
        set f [open $path r]
        fconfigure $f -encoding utf-8
        set text [read $f]
        close $f
        set Path [file normalize $path]
        $Host.bar.path configure -text $Path
        wm title [winfo toplevel $Doc] [file tail $Path]
        my render $text
    }
    # Reload keeps the reader's place: the scroll position, and the folds
    # by heading title, so a file under edit does not unfold on every save.
    method reload {} {
        if {$Path eq ""} return
        set view [lindex [$Text yview] 0]
        set folded [list]
        for {set n 0} {$n < [my region_count]} {incr n} {
            if {[my folded $n]} { lappend folded [dict get [my payload $n] title] }
        }
        my open_file $Path
        my batch {
            for {set n 0} {$n < [my region_count]} {incr n} {
                if {[dict get [my payload $n] title] in $folded} { my fold $n }
            }
        }
        $Text yview moveto $view
    }
    method open_dialog {} {
        set path [tk_getOpenFile -parent [winfo toplevel $Doc] \
            -filetypes {{Markdown {.md .markdown}} {All {*}}}]
        if {$path ne ""} { my open_file $path }
    }
    # An image path relative to the open file, as a Tk image; "" when the
    # file is missing or not a format Tk reads, so the alt text stands in.
    method image_for {path} {
        if {[dict exists $Images $path]} { return [dict get $Images $path] }
        set full [file join [file dirname $Path] $path]
        if {[catch {image create photo -file $full} img]} { set img "" }
        dict set Images $path $img
        return $img
    }

    # ---- rendering ----
    method render {text} {
        my reset
        ::tkdown::forget $Text
        dict for {path img} $Images { if {$img ne ""} { image delete $img } }
        set Images [dict create]
        set Anchors [dict create]
        my batch {
            foreach seg [::tkdown::segment_headings $text] {
                lassign $seg kind payload
                if {$kind eq "heading"} {
                    my open_section {*}$payload
                    continue
                }
                set body [string trim $payload \n]
                if {$body eq ""} continue
                set m [my append_open]
                ::tkdown::body $Text $m $body body {body code}
                my append_close $m
            }
            if {[my live] >= 0} { my region_close }
        }
        my measure
    }
    method open_section {level title} {
        if {[my live] >= 0} { my region_close }
        set n [my region_open [dict create level $level title $title]]
        set slug [heading_slug $title]
        set unique $slug
        for {set i 1} {[dict exists $Anchors $unique]} {incr i} { set unique "$slug-$i" }
        dict set Anchors $unique $n
        set m [my append_open]
        my emit $m "▾ " [list hdr h$level]
        ::tkdown::runs $Text $m $title [list hdr h$level]
        my emit $m "\n" [list hdr h$level]
        my append_close $m
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

    # ---- links ----
    method link_click {x y} {
        set url [::tkdown::link_at $Text [$Text index @$x,$y]]
        if {$url ne ""} { my follow_link $url }
    }
    method follow_link {url} {
        if {[regexp {^[a-z][a-z0-9+.-]*:} $url]} {
            exec xdg-open $url &
            return
        }
        lassign [split $url #] path anchor
        if {$path ne ""} {
            set path [file join [file dirname $Path] $path]
            if {$path ne $Path} { my open_file $path }
        }
        if {$anchor ne ""} { my goto_anchor $anchor }
    }
    method goto_anchor {anchor} {
        set anchor [string tolower $anchor]
        if {![dict exists $Anchors $anchor]} return
        set n [dict get $Anchors $anchor]
        my reveal [dict get [my region_info $n] start] top
    }

    # ---- the measure: margins follow the pane width ----
    # tkdown lays the measure under everything it paints from -margin; the
    # viewer's own header lines carry it themselves, and code blocks sit
    # one em inside it.
    method measure_later {} {
        if {$MeasureTok ne ""} return
        set MeasureTok [after idle [list [self] measure]]
    }
    method measure {} {
        set MeasureTok ""
        set width [winfo width $Text]
        if {$width <= 1} return
        set em [font measure [dict get $Fonts body] "0"]
        set margin [expr {max(12, ($width - 2 * [$Text cget -padx] - 90 * $em) / 2)}]
        $Text tag configure hdr -lmargin1 $margin -lmargin2 $margin -rmargin $margin
        set inset [expr {$margin + $em}]
        $Text tag configure code -lmargin1 $inset -lmargin2 $inset -rmargin $inset
        ::tkdown::refit $Text -margin [list $margin $margin]
    }
}

pack [ttk::frame .f] -fill both -expand 1
set viewer [Viewer new .f]
if {[llength $argv]} { $viewer open_file [lindex $argv 0] }
