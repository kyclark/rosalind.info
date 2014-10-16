import System.IO
import System.Environment   
import Data.List  
import Data.String.Utils

main = do
    (file:_) <- getArgs
    putStrLn file
    c <- readFile file
    putStrLn c
    report (countBases c)
  
--main = getArgs >>= input >>= countBases >>= putStrLn report
--
--parse :: String -> String
--parse [] = getContents
--parse fs = concat `fmap` mapM readFile fs

--parse :: String -> String
--input file = 
--    return c <- readFile file

countBases :: String -> [Int]
countBases s = map (\a -> length a) $ group $ sort $ strip s

--report :: [a] -> String
--report [] = "No usage output"
--report xs = intersperse " " (map show xs)
report xs = join ", " $ map show xs
