#!/usr/bin/env perl6

sub MAIN(Str $string1, Str $string2) {
    my $dist = abs($string1.chars - $string2.chars);

    for $string1.comb Z $string2.comb -> ($l1, $l2) {
        $dist++ if $l1 ne $l2;
    }

    say "dist $dist";
}
