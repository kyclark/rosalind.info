#!/usr/bin/env perl6

sub MAIN (Int $n where 0 < * <= 40, Int $k where 0 < * <= 5 = 1) {
    say "months ($n) litter ($k) = {fib($n, $k)}";
}

sub fib (Int $n, Int $k) {
    given $n {
        when { $_ <= 2 } { 1 }
        default { fib($n - 1, $k) + fib($n - 2, $k) * $k }
    }
}
