#!/usr/bin/env perl6

use lib '../lib';
use FastaParser;

sub MAIN (Str $fasta) {
    my @seqs = parse_file($fasta).map(-> [$id, $seq] { $seq });
    my $max  = [max] @seqs>>.chars;
    my $nseqs = @seqs.elems;
    put "nseqs $nseqs, max ($max)";

    if ($max < 2) {
        die "No sequence long enough";
    }

    my $bag-channel = Channel.new;
    say "spinning up react block";
    my $p = start {
        react {
            whenever $bag-channel -> [$bag, $k] {
                if $bag.grep(*.value == $nseqs).map(*.keys) -> @matches {
                    say "$k = {@matches}";
                    done();
                }
            }
        }
    }

    say "feeding channel";
    (2..$max).map: -> $k {
        start {
            $bag-channel.send: [ bag(@seqs.map(-> $seq { kmers($seq, $k) })), $k ];
        }
    }

    say "awaiting a react promise";
    await $p;

    say "closing the bag";
    $bag-channel.close;
}

sub kmers (Str $string, Int $k) {
    (for 0..^($string.chars - $k + 1) -> $i { $string.substr($i, $k) }).unique;
}

#    for 2..$max -> $k {
#        my $bag = bag @seqs.map(-> $seq { kmers($seq, $k) });
#        my @matches = $bag.grep(*.value == $nseqs).map(*.key) or last;
#        put "$k = {@matches.pick}";
#    }

#    my @kmers;
##    dd @match;
#    for 0..^($string.chars - $k + 1) -> $i { 
#        my $mer = $string.substr($i, $k);
#
#        if !@match || (@match && $mer ~~ /@match/) {
#            @kmers.push($mer) 
#        }
#    }
#    @kmers.unique;
#}
