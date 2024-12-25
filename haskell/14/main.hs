module Foo where

import Data.Char (isDigit)
import Control.Exception (throw)
import GHC.Read (readField)

data Quadrant = NW | NE | SE | SW deriving (Eq, Show)

-- -- test size
-- xSize = 11
-- ySize = 7

-- actual size
xSize = 101
ySize = 103


-- number extractor stolen from friend.
extractNumbers :: String -> [Int]
extractNumbers [] = []
extractNumbers string
  | null numbers = []
  | otherwise = read numbers : extractNumbers rest
  where
    (numbers, rest) = span isDigitOrNegative (dropWhile (not . isDigitOrNegative) string)
    isDigitOrNegative c = isDigit c || c == '-'

computeMagicNumbers :: [Int] -> (Int, Int)
computeMagicNumbers [startingX, startingY, rateX, rateY] =
    (xResult, yResult)
    where
        xResult = computeOneDim startingX rateX xSize
        yResult = computeOneDim startingY rateY ySize
computeMagicNumbers _ = error "needed 4 ints" -- didn't get 4 ints.

computeOneDim :: Int -> Int -> Int -> Int
computeOneDim startingPos velocity size =
    (startingPos + (velocity * 100)) `mod` size

computeQuadrant :: (Int, Int) -> Maybe Quadrant
computeQuadrant (x, y)
    | isEast && isNorth = Just NE
    | isWest && isNorth = Just NW
    | isEast && isSouth = Just SE
    | isWest && isSouth = Just SW
    | otherwise = Nothing
    where
        isEast = x > (xSize `div` 2)
        isWest = x < (xSize `div` 2)
        isSouth = y > (ySize `div` 2)
        isNorth = y < (ySize `div` 2)



-- multiply total counts per quadrant
scoreQuadrants :: [Maybe Quadrant] -> Int
scoreQuadrants [] = 0
scoreQuadrants maybeQs =
    multiplier $ quadCounter maybeQs
    where
        addHelper :: (Int, Int, Int, Int) -> (Int, Int, Int, Int) -> (Int, Int, Int, Int)
        addHelper (a1,b1,c1,d1) (a2,b2,c2,d2) = (a1+a2,b1+b2,c1+c2,d1+d2) 
        quadCounter :: [Maybe Quadrant] -> (Int, Int, Int, Int)
        quadCounter [] = (0, 0, 0, 0)
        quadCounter (Nothing : rest) = quadCounter rest
        quadCounter (Just NW : rest) = addHelper (1,0,0,0) $ quadCounter rest
        quadCounter (Just NE : rest) = addHelper (0,1,0,0) $ quadCounter rest
        quadCounter (Just SE : rest) = addHelper (0,0,1,0) $ quadCounter rest
        quadCounter (Just SW : rest) = addHelper (0,0,0,1) $ quadCounter rest
        multiplier :: (Int, Int, Int, Int) -> Int
        multiplier (a1,b1,c1,d1) = a1 * b1 * c1 * d1



-- go from strings to score
scoreInput :: [String] -> Int
scoreInput = scoreQuadrants . map (computeQuadrant . computeMagicNumbers . extractNumbers)

-- now for impure stuff
main :: IO ()
main = do
    contents <- lines <$> readFile "input.txt"
    print . scoreInput $ contents