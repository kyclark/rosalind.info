#!/usr/bin/env perl

use strict;
use File::Basename 'basename';
use List::Util 'min';

unless (@ARGV == 2) {
    printf "Usage:\n  %s <string1> <string2>\n", basename($0);
}

my ($string1, $string2) = @ARGV;
my $shortest = min(length($string1), length($string2));
my $dist     = abs(length($string1) - length($string2));

for my $i (0 .. $shortest - 1) {
    if (substr($string1, $i, 1) ne substr($string2, $i, 1)) {
        $dist++;
    }
}

print "dist = $dist\n";

sub abs {
    my $n = shift;
    return $n < 0 ? -$n : $n;
}
