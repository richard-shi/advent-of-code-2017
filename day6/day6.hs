-- Solution to Advent of Code 2017 Day 6 Part 1
import Data.List (elemIndex)
import Data.Maybe (fromJust)
import Data.Set (Set)
import Data.Map (Map)
import qualified Data.Set as Set
import qualified Data.Map as Map
import ListZipper

-- Debug
-- import Debug.Trace

incrementFirstN :: (Num a, Show a) => Int -> ListZipper a -> ListZipper a
incrementFirstN 0 x = x
incrementFirstN n x =
    incrementFirstN (n - 1) $ goForwardLoopBack $ update ((+1) $ get x) x

-- Distribute a number of increments
distribute :: Int -> Int -> [Int] -> [Int]
distribute n pos xs =
    distributeExtra extraInc pos $ map (+commonInc) xs
    where len = length xs
          commonInc = quot n len
          extraInc = mod n len

-- Distribute extra increments
distributeExtra :: Int -> Int -> [Int] -> [Int]
distributeExtra n pos xs =
    toList $ incrementFirstN n $ goToIndex pos $ fromList xs

-- Get next state of computation
nextState :: [Int] -> [Int]
nextState xs = distribute max startFrom $ toList $ updateAt pos 0 $ fromList xs
    where max = maximum xs
          pos = fromJust $ elemIndex max xs
          startFrom =
            if pos + 1 == (length xs)
                then 0
                else pos + 1


-- Return number of steps until repetition seen
seenOld :: [Int] -> Int
seenOld xs = seenSetCount 0 Set.empty xs

seenOldLoop :: [Int] -> Int
seenOldLoop xs = seenLoopCount 0 Map.empty xs

seenSetCount :: Int -> Set [Int] -> [Int] -> Int
seenSetCount count set xs =
    if Set.member xs set
        then count
        else seenSetCount (count + 1) (Set.insert xs set) (nextState xs)

seenLoopCount :: Int -> Map [Int] Int -> [Int] -> Int
seenLoopCount count m xs =
    if Map.member xs m
        then count - (fromJust $ Map.lookup xs m)
        else seenLoopCount (count + 1) (Map.insert xs count m) (nextState xs)

main = do
    let initial = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
    print $ seenOldLoop initial

