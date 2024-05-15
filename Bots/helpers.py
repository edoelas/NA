from Classes.Constants import *
from Classes.Materials import Materials
from typing import List
import random

TOWN = BuildConstants.TOWN
CITY = BuildConstants.CITY
ROAD = BuildConstants.ROAD   
CARD = BuildConstants.CARD

CEREAL = MaterialConstants.CEREAL
MINERAL = MaterialConstants.MINERAL
CLAY = MaterialConstants.CLAY
WOOD = MaterialConstants.WOOD
WOOL = MaterialConstants.WOOL

# cereal, mineral, clay, wood, wool
building_costs = {
    TOWN: Materials(1, 0, 1, 1, 1), # {CEREAL: 1, CLAY: 1, WOOD: 1, WOOL: 1},
    CITY: Materials(2, 3, 0, 0, 0), # {CEREAL: 2, MINERAL: 3},
    ROAD: Materials(0, 0, 1, 1, 0), # {CLAY: 1, WOOD: 1},
    CARD: Materials(1, 1, 0, 0, 1), # {CEREAL: 1, WOOL: 1, MINERAL: 1}
}

goals_costs = {
    "build_town": building_costs[TOWN],
    "build_city": building_costs[CITY],
    "build_road": building_costs[ROAD],
    "buy_card": building_costs[CARD]
}


def subl(list1, list2):
    """
    Subtract corresponding elements of two lists and return the result as a new list.
    """
    return [x - y for x, y in zip(list1, list2)]


def addl(list1, list2):
    """
    Adds corresponding elements of two lists and returns a new list.
    """
    return [x + y for x, y in zip(list1, list2)]


def posl(list1):
    """
    Returns a new list with only the positive elements of the input list.
    """
    return [x if x > 0 else 0 for x in list1]

def index_to_list(index, value = 1):
    """
    Converts an index to a list with the value at the index.
    """
    return [value if i == index else 0 for i in range(5)]

def wighted_index_choice(weights):
    """
    Chooses an index based on the weights.
    """
    list = [0] * weights[0] + [1] * weights[1] + [2] * weights[2] + [3] * weights[3] + [4] * weights[4]
    return random.choice(list)

def material_to_list(materials):
    """
    Converts a Materials object to a list.
    """
    return [materials.cereal, materials.mineral, materials.clay, materials.wood, materials.wool]


    
def missing_materials(owned: Materials, wanted: Materials):
    dif = subl(material_to_list(wanted), material_to_list(owned))
    return Materials(*posl(dif))


def excess_materials(owned: Materials, goal_list: List[str]):
    """
    Calculates the excess materials based on the owned materials and the desired goals.
    """
    excess = material_to_list(owned)
    for goal in goal_list:
        goal = material_to_list(goals_costs[goal])
        excess = subl(excess, goal)
    
    return Materials(*posl(excess))


def create_exchange(owned: Materials, goal_list: List[str]):
    """
    Creates a trade offer based on the owned materials and the desired goals.
    """
    excess = excess_materials(owned, goal_list)
    wanted = [0, 0, 0, 0, 0]
    for goal in goal_list:
        goal = material_to_list(goals_costs[goal])
        wanted = addl(wanted, goal)
    needed = missing_materials(owned, Materials(*wanted))
    return excess, needed


