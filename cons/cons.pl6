#!/usr/bin/env perl6

sub MAIN (Str $filename) {
    my Str @seqs = get_seqs($filename);
    my Int $max  = @seqs.map({.chars}).max;
    my %matrix;
    my Str $consensus;
    for 0..^$max -> $i { 
        my $bases   = (for @seqs -> $seq { $seq.substr($i,1) }).Bag;
        for <A C T G> -> $base {
            %matrix{ $base }.push($bases{ $base });
        }
        my $n       = $bases.values.max;
        $consensus ~= $bases.grep({ .value == $n }).map({.key}).head; 
    }

    say $consensus;
    for <A C G T> -> $base {
        say "$base: ", %matrix{ $base }.join(' ');
    }
}

sub get_seqs(Str $filename) {
    my @seqs;
    my $buffer;
    my $add = sub ($buf) { @seqs.push($buf) if $buf };

    for $filename.IO.lines -> $line {
        if ($line.substr(0,1) eq '>') {
            &$add($buffer);
            $buffer = '';
        }
        else {
            $buffer ~= $line;
        }
    }
    &$add($buffer);

    @seqs;
}
