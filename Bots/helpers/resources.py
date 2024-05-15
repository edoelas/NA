from Classes.Constants import *

TOWN = BuildConstants.TOWN
CITY = BuildConstants.CITY
ROAD = BuildConstants.ROAD   
CARD = BuildConstants.CARD

CEREAL = MaterialConstants.CEREAL
MINERAL = MaterialConstants.MINERAL
CLAY = MaterialConstants.CLAY
WOOD = MaterialConstants.WOOD
WOOL = MaterialConstants.WOOL

building_costs = {
    TOWN: {CEREAL: 1, CLAY: 1, WOOD: 1, WOOL: 1},
    CITY: {CEREAL: 2, MINERAL: 3},
    ROAD: {CLAY: 1, WOOD: 1},
    CARD: {CEREAL: 1, WOOL: 1, MINERAL: 1}
}
