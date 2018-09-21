module P006 where
--     Find the difference between the sum of the squares of the first one hundred
--      natural numbers and the square of the sum.

p006 :: Int
p006 =  sum [1..100] ^2 - sum (map (^2) [1..100])
