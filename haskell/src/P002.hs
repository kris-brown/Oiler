module P002 where

-- Finds the sum of the even-valued Fibonacci terms < 4e6
p002 :: Int
p002 = sum $ filter even $ takeWhile (<4000000) fibs

fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
