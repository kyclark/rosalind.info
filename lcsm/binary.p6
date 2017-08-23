#!/usr/bin/env perl6

for ((4, 10..20), (5, 1..100), ('d', 'a'..'z'), ('a', 1..10)) -> ($n, $list) {
    put "n ($n), list ({$list.join(', ')})";

    given my $val = search($n, $list) {
        when Failure { put "NOT FOUND" }
        default { put "val ($val)" }
    }
}

multi search($n, []) { fail }

multi search($n, [$x]) { return $n cmp $x == Same ?? $x !! fail }

multi search($n, @x) {
    my $len = @x.elems;
    my $mid = floor($len / 2);
    fail if $mid == 0;
    my $val = @x[$mid];
    put "n = $n, len ($len) mid ($mid), val ($val)";

    given $n cmp $val {
        when Same { $val }
        when Less { search($n, @x[^$mid])   }
        default   { search($n, @x[$mid..*]) }
    }
}
