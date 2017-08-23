#!/usr/bin/env perl6

sub MAIN (*@args) { 
    say trend(@args);
#    CATCH { say 'failure: ' ~ $ret.exeception.message }
#    dd $ret;

#    given $ret {
#        when Failure { say 'fail: ' ~ $ret.message }
#        default { say $ret }
#    }
}

sub trend (@args) {
    fail "too short {@args.elems}" if @args.elems < 2;
    my ($x, $y) = @args[*-2, *-1];
    return $x - $y < 0 ?? 'up' !! 'down';
}
