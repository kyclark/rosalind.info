#!/usr/bin/env perl6

use lib '.';
use FastaParser;

sub MAIN (Str $filename, Int $k where * > 0 = 3) {
    my (%prefix, %suffix);
    for parse_file($filename) -> [$id, $seq] {
        %prefix{ $seq.substr(0, $k) }.push($id);
        %suffix{ $seq.substr($seq.chars - $k) }.push($id);
    }

    for %prefix.kv -> $pre, @ids {
        next unless %suffix{ $pre }.defined;
        for @ids -> $id {
            for %suffix{$pre}.grep(* ne $id).list -> $other_id {
                say ($other_id, $id).join(' ');
            }
        }
    }
}
