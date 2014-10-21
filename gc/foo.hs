main = do
    f <- readFasta "input.fasta"
    putStrLn (seqheader f)
