#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';
use autodie;

my $seq = join '', map { chomp && $_ } <>;
$seq =~ s/T/U/g;
say $seq;
