input = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]


-- distribute :: Int -> [Int] -> [Int]
-- distribute 0 x = x
-- distribute _ [] = []
-- distribute n (x:xs) = (x + 1) : distribute (n - 1) xs




-- redistribute :: [Int] -> [Int]
-- redistribute x =

main = do
    putStrLn "Starting program"
    let l = distribute 2 [1, 2, 3]
    putStrLn $ show l
