#!/usr/bin/env perl6

sub MAIN(Str $string1, Str $string2) {
    say [+] $string1.comb <<ne>> $string2.comb;
}
