#!/usr/bin/env perl6

sub MAIN(Str $string1, Str $string2) {
    my $shortest = min($string1.chars, $string2.chars);
    my $dist     = abs($string1.chars - $string2.chars);

    for 0..^$shortest -> $i {
        if ($string1.substr($i, 1) ne $string2.substr($i, 1)) {
            $dist++;
        }
    }

    say "dist $dist";
}
