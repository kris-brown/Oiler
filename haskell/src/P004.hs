module P004 where
-- Find largest pallindrome product of two 3-digit numbers
p004 :: Int
p004 = maximum $ filter (pdrome . show) [i*j | i <- [100..999], j<-[i..999]]

pdrome :: String -> Bool
pdrome x = reverse x == x
