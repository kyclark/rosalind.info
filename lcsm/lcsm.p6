#!/usr/bin/env perl6

use lib '../lib';
use FastaParser;

PROCESS::<$SCHEDULER> = ThreadPoolScheduler.new(initial_threads => 0, max_threads => 2);

# main entry point
sub MAIN (Str $fasta) {
    my @seqs  = parse_file($fasta).map(-> [$id, $seq] { $seq });
    my $max   = @seqs.map(*.chars).max;
    my $nseqs = @seqs.elems;
    put "nseqs $nseqs, max ($max)";

    for @list -> $n {
	thie
    }

    if ($max < 2) {
        die "No sequence long enough";
    }

    my $k = $max;
    my (@pastn, @pastk, @x);

    loop {
        my $bag     = bag @seqs.map(-> $seq { kmers($seq, $k) });
        my @matches = $bag.grep(*.value == $nseqs).map(*.key);
        my $nmatch  = @matches.elems;
        put "k ($k) matches = $nmatch";
        @pastk.push($k);
        @x.push($k => $nmatch);
        dd @x.sort;

        my $direction;
        if $k == 1 {
            put "Bottomed out";
            last;
        }
        elsif $nmatch == $nseqs {
            put "$k = {@matches.pick}";
            last;
        }

        #my $lastn = @pastn.elems ?? @pastn[*-1] !! $nmatch;

        if $nmatch == 0 {
            my $lastn = @x.elems > 0 ?? @x.grep(*.key < $k).sort.first.key !! $nmatch;
            $k -= floor($k/2);
        }
        elsif $nmatch == $nseqs {
            $k++;
        }
        else {
            my $lastn = @x.elems > 0 ?? @x.grep(*.key > $k).sort.first.key !! $nmatch;
            put "last = $lastn";
            $k += floor(($lastn - $k)/2);
        }

        @pastn.push($nmatch);
    }

}

sub kmers (Str $string, Int $k) {
    (for 0..^($string.chars - $k + 1) -> $i { $string.substr($i, $k) }).unique;
}
