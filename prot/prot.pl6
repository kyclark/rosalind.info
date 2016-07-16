#!/usr/bin/env perl6

my %codons = 
    'AAA' => 'K', 'AAC' => 'N', 'AAG' => 'K', 'AAU' => 'N',
    'ACA' => 'T', 'ACC' => 'T', 'ACG' => 'T', 'ACU' => 'T',
    'AGA' => 'R', 'AGC' => 'S', 'AGG' => 'R', 'AGU' => 'S',
    'AUA' => 'I', 'AUC' => 'I', 'AUG' => 'M', 'AUU' => 'I',
    'CAA' => 'Q', 'CAC' => 'H', 'CAG' => 'Q', 'CAU' => 'H',
    'CCA' => 'P', 'CCC' => 'P', 'CCG' => 'P', 'CCU' => 'P',
    'CGA' => 'R', 'CGC' => 'R', 'CGG' => 'R', 'CGU' => 'R',
    'CUA' => 'L', 'CUC' => 'L', 'CUG' => 'L', 'CUU' => 'L',
    'GAA' => 'E', 'GAC' => 'D', 'GAG' => 'E', 'GAU' => 'D',
    'GCA' => 'A', 'GCC' => 'A', 'GCG' => 'A', 'GCU' => 'A',
    'GGA' => 'G', 'GGC' => 'G', 'GGG' => 'G', 'GGU' => 'G',
    'GUA' => 'V', 'GUC' => 'V', 'GUG' => 'V', 'GUU' => 'V',
    'UAA' => 'Stop', 'UAC' => 'Y', 'UAG' => 'Stop', 'UAU' => 'Y',
    'UCA' => 'S', 'UCC' => 'S', 'UCG' => 'S', 'UCU' => 'S',
    'UGA' => 'Stop', 'UGC' => 'C', 'UGG' => 'W', 'UGU' => 'C',
    'UUA' => 'L', 'UUC' => 'F', 'UUG' => 'L', 'UUU' => 'F',
;

sub MAIN (Str $string) {
    my $rna = $string.IO.e ?? $string.IO.slurp !! $string;
    my @res = (for $rna ~~ m:global/. ** 3/ -> $codon {
            my $res = %codons{$codon};
            last if $res eq 'Stop';
            $res;
        }
    );

    say @res.join;
}
