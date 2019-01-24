module Reverse where 
rev :: [t]->[t]
rev [] = []
rev m = rev(tail m) ++ head m : []