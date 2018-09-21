module P007 where

import           Lib (primes)

-- Find the 10001st prime
p007 :: Int
p007 =   primes !! 10000
