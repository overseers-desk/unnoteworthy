# Corrections clerk: after the blind second coding

Read `briefs/standing-brief-block.md` first, then `0-comparables/codebook-v1.md`, then `0-comparables/second-coding.md`, then `0-comparables/second-coding-sample.md`, then for each sampled slug its profile under `0-comparables/products/`, its row in `0-comparables/coded-corpus.tsv` and its row in `0-comparables/second-coding.tsv`. Nothing else in the repository is open to you, and no web page.

The method re-codes a mechanical sample blind and orders corrections before any synthesis. The agreement file lists every cell where the first coding and the second differ. Sort the differences into three kinds and act on each:

1. **Format, not coding.** The two clerks coded the same value in different words or order: a list of forms or channels in another order, a date written another way, a quote attached differently, a sub-field laid out differently. No correction; count them.
2. **Rule, applied differently.** The codebook's rule decides the case and one clerk misapplied it. Correct the first coding's cell in `coded-corpus.tsv` to the value the rule gives, keeping the quote, and record the correction. Where the second coding is the one in error, record that and change nothing.
3. **Rule, cannot decide.** Two careful clerks read the rule differently and the rule does not settle it. Change nothing; record the variable and the case as a weakness of the frozen codebook, since a frozen rule changes only by a version, a date and a re-coding of everything coded, which this run does not undertake.

Write `0-comparables/corrections.md`: the counts by kind and by variable; the list of corrections applied, one line each (slug, variable, from, to, the rule); the list of second-coding errors left as they stand; and the list of codebook weaknesses with the rule each would need, for the synthesis clerk to carry into a finding about the instrument. Then apply the corrections to `coded-corpus.tsv` in place, touching only the cells you list. Your final message gives the three counts, the number of cells corrected, and the variables whose agreement a reader should weigh as weak.
