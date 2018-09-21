module Main where

import           Data.Map (fromList)
import           Lib
import           P001
import           P002

problems :: Show a => Map Int a
problems = fromList [(1,P001),(2,P002)]

main :: IO ()
main = do [probNumber] <- getArgs
          putStrLn $ problems ! probNumber

P001 = sum $ filter f [1..1000]
 where f i = (i // 3 ==0 )|| (i // 5 == 0)
