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

unless (defined $n && $n > 0 && $n <= $max_n) {
    die sprintf("Bad n (%s) :: 0 < n <= $max_n\n", defined $n ? $n : 'undef');
}

unless (defined $k && $k > 0 && $k <= $max_k) {
    die sprintf("Bad k (%s) :: 0 < k <= $max_k\n", defined $k ? $k : 'undef');
}

# e.g., k=1: 1 1 2 3  5  8  13
# e.g., k=3: 1 4 4 7 11 18 29
my $total;
my @series = (1, $k); # initialize the series
for my $i (1..$n) {
     $total = sum(@series);
     shift @series; 
     push @series, $total; 
}

say "(n :: $n, k :: $k) -> $total";

sub sum {
    my $sum = 0;
    map { $sum += $_ } @_;
    print join(' + ', @_), " = $sum\n";
    return $sum;
}
