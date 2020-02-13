# Implement a class to hold room information. This should have name and
# description attributes.

from src.item import *

class Room:
    name = ""
    description = ""
    items = []
    #
    # * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    #   which point to the room in that respective direction.

    n_to = ""
    s_to = ""
    w_to = ""
    e_to = ""



    def __init__(self, name, description):
        self.name = name
        self.description = description


#List of rooms

listOfRooms = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

listOfRooms['outside'].n_to = listOfRooms['foyer']
listOfRooms['foyer'].s_to = listOfRooms['outside']
listOfRooms['foyer'].n_to = listOfRooms['overlook']
listOfRooms['foyer'].e_to = listOfRooms['narrow']
listOfRooms['overlook'].s_to = listOfRooms['foyer']
listOfRooms['narrow'].w_to = listOfRooms['foyer']
listOfRooms['narrow'].n_to = listOfRooms['treasure']
listOfRooms['treasure'].s_to = listOfRooms['narrow']

# distribute room treasure
listOfRooms['treasure'].items = [listOfItems['gold']]
listOfRooms['foyer'].items = [listOfItems['goop'], listOfItems['vaporizer']]
listOfRooms['overlook'].items = [listOfItems['money']]
