#!/usr/bin/env perl6

sub MAIN (Str $input, Str $pattern) {
    my Str $string = $input.IO.e ?? $input.IO.slurp !! $input;
    my $n = $pattern.chars;

    my @locs;
    for 0..$string.chars -> $i {
        if $string.substr($i, $n) eq $pattern { @locs.push: $i + 1 }
    }

    say @locs.join(' ');
}
