import Data.XML.Pickle

data Appartement = Appartement {
	id :: Int,
	place :: String,
	city :: String,
	area :: Int,
	numRooms :: Int,
	yearCreated :: Int,
	price :: Int
}

generateRecord =


main :: IO ()
main = do
	print $ pickle (generateRecord (Appartement {id=1, place="Heltmana", city="Kraków", area="Podgórze", area=120, numRooms=5, yearCreate=1990, price=1000000}))
