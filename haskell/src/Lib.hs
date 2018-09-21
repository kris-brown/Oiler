module Lib
    ( prime, primes
    ) where

someFunc :: IO ()
someFunc = putStrLn "someFunc"

prime :: Int -> Bool
prime n = length (takeWhile divides factors) == length factors
 where
   divides d = n `mod` d /= 0
   sqrt_n    = round $ sqrt $ fromIntegral n
   factors   =  [2 .. sqrt_n]

primes :: [Int]
primes = filter prime [2..]
