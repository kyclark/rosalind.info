unit module Binary;

#subset Direction of Str where * ~~ m:i/<(up|down)>/;

#enum Direction <Up Down>;

sub search (Int $n, @list) is export {
    say "n ($n), list = ", @list;
}

#    my $top = $n %% 2 ?? $n !! $n - 1;

#    sub half (Int $x) {
#        my $y = $x / 2;        
#        if ($y > 1) {
#            return $y, half($y);
#        }
#    }
#
#    ($n, $top/
#}
