module P012 where
import           Lib (sqrt')
p012 :: Int
p012 =  head [t | t <- triangle,div500 t]

div500 :: Int -> Bool
div500 i = length (divisors i) > 500

divisors :: Int -> [Int]
divisors i =  [ x | x <- [2..ceiling (sqrt' i)], i `quot` x == 0]

-- same trick as fibonacci
triangle :: [Int]
triangle = 1 : zipWith (+) triangle [2..]
