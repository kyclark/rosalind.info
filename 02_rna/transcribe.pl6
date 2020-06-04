#!/usr/bin/env perl6

sub MAIN (Str $string) {
    my $dna = $string.IO.e ?? $string.IO.slurp !! $string;
    say $dna.subst('T', 'U');
}
