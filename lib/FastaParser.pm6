unit module FastaParser;

sub parse_file (Str $filename) is export {
    my (@seqs, $header, $buffer);
    sub add($hdr, $buf) { @seqs.push(($hdr, $buf)) if $buf };

    for $filename.IO.lines -> $line {
        if ($line.substr(0,1) eq '>') {
            add($header, $buffer);
            $header = $line.substr(1);
            $buffer = '';
        }
        else {
            $buffer ~= $line;
        }
    }
    add($header, $buffer);

    return @seqs;
}
