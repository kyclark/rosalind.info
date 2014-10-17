import System.Environment

main = do
    [f] <- getArgs
    putStrLn f
    c <- readFile f
    putStrLn c
    --putStrLn (lines $ read c)
