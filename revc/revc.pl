#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

my $seq = join '', reverse map { chomp && split '' } <>;
$seq =~ tr/ACGT/TGCA/;
say $seq;
