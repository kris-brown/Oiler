module P009 where
import           Lib (sqrt', square)

-- |  There exists exactly one Pythagorean triplet (a^2+b^2=c^2, a<b<c) for which
--    a + b + c = 1000. Find the product abc.
--    a+b+sqrt(a^2+b^2)

p009 :: Int
p009 = head [a*b*c | a<-[100..1000],
                     b <- [a+1..1000],
                     square (a^2+b^2),
                     let c = round (sqrt' (a^2+b^2)),
                     1000 == a + b + c]
