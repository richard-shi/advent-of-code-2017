import Data.Sequence
import Data.List

input = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]

replaceLargest :: Int -> [Int] -> [Int]
replaceLargest n xs = update elemIndex (maximum xs) xs


distribute :: Int -> [Int] -> [Int]
distribute n xs = map (+1) xh ++ xt
    where (xh, xt) = splitAt n xs

redistribute :: [Int] -> [Int]
redistribute x =
    where

main = do
    putStrLn "Starting program"
    let l = distribute 2 [5, 4, 3]
    putStrLn $ show l
