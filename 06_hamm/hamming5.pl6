#!/usr/bin/env perl6

sub MAIN(Str $string1, Str $string2) {
    say +StrDistance.new(:before($string1), :after($string2));
}
