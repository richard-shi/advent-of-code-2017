-- Solution to Advent of Code 2017 Day 6 Part 1
import Data.List

input = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]

data Side = LeftSide | RightSide

-- Get opposite side
flipSide :: Side -> Side
flipSide LeftSide = RightSide
flipSide RightSide = LeftSide

-- Increment the first n numbers in a list
incrementFirstN :: Int -> [Int] -> [Int]
incrementFirstN 0 xs = xs
incrementFirstN _ [] = []
incrementFirstN n (x:xs) = (x + 1) : incrementFirstN (n - 1) xs

-- Distribute a number of increments
distribute :: Int -> Int -> [Int] -> [Int]
distribute n pos xs = distributeExtra extraInc $ splitAt pos $ map (+commonInc) xs
    where len = length xs
          commonInc = quot n len
          extraInc = mod n len

-- Distribute extra increments
distributeExtra :: Int -> ([Int], [Int]) -> [Int]
distributeExtra n tup = _distributeExtra n LeftSide tup

-- Helper for distributing extra increments
-- Side variable keeps track of which list is currently being incremented
_distributeExtra :: Int -> Int -> Side -> ([Int], [Int]) -> [Int]
_distributeExtra n pos (h:hs, t:ts) =

-- _distributeExtra :: Int -> Side -> ([Int], [Int]) -> [Int]
-- _distributeExtra 0 LeftSide (h,t) = h ++ t
-- _distributeExtra 0 RightSide (h,t) = h ++ t
-- _distributeExtra n LeftSide (h,t) = _distributeExtra (n - 1) RightSide ([], [])

main = do
    print "Incrementing the First N elements"
    print $ incrementFirstN 3 [0, 0, 0, 0, 0, 0]

