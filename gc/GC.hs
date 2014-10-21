import System.Environment
import System.Exit
import Bio.Sequence.Fasta

main = getArgs >>= parse >>= putStr . gc

parse ["-h"] = usage   >> exit
parse ["-v"] = version >> exit
parse []     = getContents
parse fs     = concat `fmap` mapM readFile fs

usage   = putStrLn "Usage: gc [-vh] [file ..]"
version = putStrLn "gc 0.1"
exit    = exitWith ExitSuccess
die     = exitWith (ExitFailure 1)

gc s = s
