#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';
use autodie;
use Data::Dump 'dump';

chomp(my $dna = <>);
my %base;
map { $base{$_}++ } split(//, $dna);

say join ' ', map { $base{$_} } qw[ A C G T];
