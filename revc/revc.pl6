#!/usr/bin/env perl6

sub MAIN (Str $dna) {
    say $dna.comb.reverse.join.trans('ACTG' => 'TGAC')
}
