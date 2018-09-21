module P003 where

-- Max prime factor of 600851475143
p003 :: Int
p003 = maximum $ factorize 600851475143

factorize :: Int -> [Int]
factorize 1 = []
factorize n = lowfac : factorize (n `quot` lowfac)
  where lowfac = head $ filter (divides n) $ factors n

divides :: Int -> Int -> Bool
divides a b = a `mod` b == 0

sqrt' :: Int -> Int
sqrt' a =  ceiling (sqrt $ fromIntegral a)

factors :: Int -> [Int]
factors n = [2..sqrt' n] ++ [n]
