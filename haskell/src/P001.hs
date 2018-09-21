module P001 where

p001 :: Int
p001 = sum $ filter filt [1..1000]
 where filt i = (i `mod` 3 ==0 )|| (i `mod` 5 == 0)
