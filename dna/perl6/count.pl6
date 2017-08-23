#!/usr/bin/env perl6

# http://rosalind.info/problems/dna/

unless (@*ARGS.elems > 0) {
    die sprintf("Usage: %s string/file", $*PROGRAM-NAME);
}

my $in  = @*ARGS.shift;
my $dna = $in.IO.e ?? slurp($in).chomp !! $in;

my Int %count;
for $dna.uc.split('') { $_ && %count{$_}++ }

say join ' ', %count<A C T G> >>//>> 0;
