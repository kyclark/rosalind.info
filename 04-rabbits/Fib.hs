import System.Environment

fib :: Int -> Int -> Int
fib n k
    | n < 3 = 1
    | otherwise = (fib (n-1) k) + (k * (fib (n-2) k))

main = do
    [n,k] <- getArgs
    let x = fib (read n) (read k)
    putStrLn (show x)
