module P010 where
import           Lib (prime)
-- Find the sum of all the primes below two million.
p010 :: Int
p010 =  sum $ filter prime [2..2000000]
