module Main where

import           Data.Map           (Map, fromList, map, (!))
import           P001
import           P002
import           Prelude            hiding (map)
import           System.Environment (getArgs)

problems :: Map Int String
problems = map show $ fromList [(1,p001),(2,p002)]

main :: IO ()
main = do [i] <- getArgs
          putStrLn $ problems ! (read i :: Int)
