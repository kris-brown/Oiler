module P005 where
-- Find the LCM of 1 through 20

p005 :: Int
p005 = lcms [11..20]

lcms :: [Int]->Int
lcms [x]      = x
lcms (x:y:zs) = lcms (lcm x y : zs)
