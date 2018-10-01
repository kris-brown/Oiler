module Lib
    ( prime, primes, slice, square,sqrt'
    ) where


-- Math related
prime :: Int -> Bool
prime n = length (takeWhile divides factors) == length factors
 where
   divides d = n `mod` d /= 0
   sqrt_n    = round $ sqrt $ fromIntegral n
   factors   =  [2 .. sqrt_n]

primes :: [Int]
primes = filter prime [2..]

sqrt' :: Integral a => a -> Float
sqrt' = sqrt . fromIntegral

square :: Int -> Bool
square n = ceiling floatrt == floor floatrt
  where floatrt = sqrt' n

-- List related
slice  :: Int -> Int -> [a] -> [a]
slice from to = take (to - from) . drop from
