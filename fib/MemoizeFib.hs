import System.Environment

--fib :: Int -> Int -> Int
--fib n k
--    | n < 3 = 1
--    | otherwise = (fib (n-1) k) + (k * (fib (n-2) k))

fib :: Int -> Int 
fib n 
    | n < 3 = 1
    | otherwise = fib (n-1) + fib (n-2)

memoized_fib :: Int -> Int
memoized_fib = (map fib [0 ..] !!)

main = do
    [n,k] <- getArgs
    let x = memoized_fib (read n) -- (read k)
    putStrLn (show x)
