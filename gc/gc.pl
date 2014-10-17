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
    my $gc     = join('', grep { /[GC]/i } split('', $seq));

    push @seqs, [ sprintf('%.6f', length($gc) * 100 /length $seq), $id ];
}

close $fh;

@seqs = sort { $b->[0] <=> $a->[0] } @seqs;
print join "\n", reverse(@{ $seqs[0] }), '';

