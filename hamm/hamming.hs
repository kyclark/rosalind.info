import System.Environment (getArgs)

main :: IO ()
main = do
  list <- getArgs
--  if (length list != 2) 

  let lengths  = map length list


  let distance = abs $ foldr (-) 0 lengths + 
                 (dist $ map (take $ minimum lengths) list)
  putStrLn $ "distance = " ++ show(distance)

dist [[], []] = 0
dist [a, b] = do
  let i = if head a == head b then 0 else 1
  i + dist [(tail a), (tail b)]
