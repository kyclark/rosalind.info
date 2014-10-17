#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';
use autodie;
use Data::Dump 'dump';

my $file = shift or die "No file\n";
open my $fh, '<', $file;

my @seqs;

local $/ = '>';
while (my $chunk = <$fh>) {
    chomp $chunk;
    next unless $chunk;

    my @lines  = split /\n/, $chunk;
    my $id     = shift @lines;
    my $seq    = join('', @lines);
    my $gc     = length(join('', grep { /[GC]/i } split('', $seq)));

    push @seqs, [ $id, sprintf('%.6f', $gc * 100 /length $seq) ];
}

close $fh;

@seqs = sort { $b->[1] <=> $a->[1] } @seqs;
print join "\n", @{ $seqs[0] }, '';

