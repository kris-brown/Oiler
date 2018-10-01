module Main where

import           Data.Map           (Map, fromList, map, (!))
import           P001
import           P002
import           P003
import           P004
import           P005
import           P006
import           P007
import           P008
import           P009
import           P010
import           P011
import           P012
import           P013
import           P014
import           P015
import           P016
import           P017
import           P018
import           P019
import           P020

import           Prelude            hiding (map)
import           System.Environment (getArgs)

problems :: Map Int String
problems = map show $ fromList [(1,p001),(2,p002),(3,p003),(4,p004),(5,p005),
                                (6,p006),(7,p007),(8,p008),(9,p009),(10,p010),
                                (11,p011),(12,p012),(13,p013),(14,p014),(15,p015),
                                (16,p016),(17,p017),(18,p018),(19,p019),(20,p020)]

main :: IO ()
main = do [i] <- getArgs
          putStrLn $ problems ! (read i :: Int)
