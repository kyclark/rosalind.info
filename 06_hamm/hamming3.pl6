#!/usr/bin/env perl6

sub MAIN(Str $string1, Str $string2) {
    my @list = $string1.comb Z $string2.comb;
    my $dist = abs($string1.chars - $string2.chars) +
     (for @list -> ($a, $b) { $a eq $b ?? True !! False }).grep(*==False).elems;

    say "dist = $dist";
}
