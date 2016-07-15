#!/usr/bin/env perl6

sub MAIN (Str $string) {
    my $dna   = $string.IO.e ?? $string.IO.slurp !! $string;
    my $count = $dna.comb.Bag;
    say join ' ', $count<A C G T>;
}
