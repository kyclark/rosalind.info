#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

my $max_n = 40;
my $max_k = 5;

if (!@ARGV) {
    die "Need n (# rabbits) and k (size of litter)\n";
}

my $n = shift or die "Need n (# rabbits)\n";
my $k = shift || 1;

unless ($n > 0 && $n <= $max_n) {
    die "Bad n ($n) :: 0 < n <= $max_n\n";
}

unless ($k > 0 && $k <= $max_k) {
    die "Bad k ($k) :: 0 < k <= $max_k\n";
}

printf "(n :: %s, k :: %s) -> %s\n", $n, $k, fib($n, $k);
exit 0;

sub fib {
    my ($n, $k) = @_;
    return 1 if $n < 3;
    return fib($n - 1, $k) + $k * fib($n - 2, $k);
}
