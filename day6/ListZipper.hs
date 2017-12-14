-- An exploratory implementation of list zippers
-- Richard Shi 2017

module ListZipper where

-- (List where current element is head, previous elements)
type ListZipper a = ([a],[a])

goForward :: ListZipper a -> ListZipper a
goForward ([], bs) = ([], bs)
goForward (x:xs, bs) = (xs, x:bs)

goBackward :: ListZipper a -> ListZipper a
goBackward (xs, []) = (xs, [])
goBackward (xs, b:bs) = (b:xs, bs)

goForwardLoopBack :: ListZipper a -> ListZipper a
goForwardLoopBack ([x], bs) = goToFirst ([], x:bs)
goForwardLoopBack bs = goForward bs

goBackwardLoopBack :: ListZipper a -> ListZipper a
goBackwardLoopBack (xs, [b]) = goToLast (b:xs, [])
goBackwardLoopBack xs = goBackward xs

goToFirst  :: ListZipper a -> ListZipper a
goToFirst  (x, []) = (x, [])
goToFirst  xs = goToFirst $ goBackward xs

goToLast :: ListZipper a -> ListZipper a
goToLast ([], x) = ([], x)
goToLast xs = goToLast $ goForward xs

goToIndex :: Int -> ListZipper a -> ListZipper a
goToIndex 0 xs = xs
goToIndex n xs = goToIndex (n - 1) $ goForward xs

fromList :: [a] -> ListZipper a
fromList xs = (xs, [])

toList :: ListZipper a -> [a]
toList xs = fst $ goToFirst xs

get :: ListZipper a -> a
get (x:xs, _) = x

update :: a -> ListZipper a -> ListZipper a
-- update v ([], bs) = (v:[], bs)
update v (x:xs, bs) = (v:xs, bs)

updateAt :: Int -> a -> ListZipper a -> ListZipper a
updateAt n v xs = update v $ goToIndex n xs

remove :: ListZipper a -> ListZipper a
remove (x:xs, bs) = (xs, bs)




