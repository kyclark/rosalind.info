#!/usr/bin/env perl6

sub MAIN (Str $string) {
    my $n = $string.chars;

    my %x;
    for 0..$n-2 -> $i {
        my ($a, $b) = $string.substr($i, 2).comb;
        %x{$a}{$b}++;
    }

    dd %x;
    for %x.kv -> $first, $succ {
        for $succ.kv -> $snd, $count {
            printf "%s: %s = %.3f\n", $first, $snd, $count/($n-1);
        }
    }
}
