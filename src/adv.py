import textwrap

from src.player import Player
from src.room import Room
from src.item import listOfItems
from src.item import Item

help = """__________HELP________ 
The following are valid commands: 
n or N = travel north if possible 
w or W = travel west if possible 
e or E = travel east if possible 
s or S = travel south if possible

q or Q = quit the program 

help = open this helpful document
"""
room = {
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# distribute room treasure
room['treasure'].items = [listOfItems['gold']]
room['foyer'].items = [listOfItems['goop'], listOfItems['vaporizer']]
room['overlook'].items = [listOfItems['money']]

print(f"{room['outside'].n_to} and target should be {room['foyer']}")
if (room['outside'].n_to == room['foyer']):
    print("outside n to foyer link successful, proceeding")
else:
    print("somethings gone wrong with room linkage, exiting")
    exit("all fd up in room linkage")
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

print("Adventure game or whatever!")
mPlayer = Player(
    name=input("enter your name:"),
    currentRoom=room['outside']
)

# textwrap impl, send it text, it'll wrap and print it for ya
# edit this function to alter text wrap settings or do any other final processing on text,
# could be expanded concatanate multiple strs or whatever
tw = textwrap


def textwrapIMPL(text: str):
    final = tw.wrap(text, 80)
    for t in final:
        print(t)


# set out keep playing variable to true to figure out of we need to play another turn or not
keepPlaying = True

# welcome player
print(f"Hello {mPlayer.name}! lets get to getting")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# move to handles the assigning room location, should only get called on valid data -- i.e. n,w,s,e
# however moveTo is responsible for determining if it should actually move the player, or spit an error
def moveTo(target: Player, letter: str):
    if letter == "n":
        if target.currentRoom.n_to == "":
            textwrapIMPL(f"Sorry {mPlayer.name} there's nowhere north to go right now")
        else:
            target.currentRoom = target.currentRoom.n_to
    if letter == "s":
        if target.currentRoom.s_to == "":
            textwrapIMPL(f"Sorry {mPlayer.name} there's nowhere south to go right now")
        else:
            target.currentRoom = target.currentRoom.s_to
    if letter == "w":
        if target.currentRoom.w_to == "":
            textwrapIMPL(f"Sorry {mPlayer.name} there's nowhere west to go right now")
        else:
            target.currentRoom = target.currentRoom.w_to
    if letter == "e":
        if target.currentRoom.e_to == "":
            textwrapIMPL(f"Sorry {mPlayer.name} there's nowhere east to go right now")
        else:
            target.currentRoom = target.currentRoom.e_to

def error():
    textwrapIMPL("Invalid entry, sorry, please type help to RTFM")

def getItem(str):
    for item in mPlayer.currentRoom.items:
        if str in listOfItems and item == listOfItems[str]:
            #ADD ITEM TO PLAYERS LIST
            mPlayer.items.append(item)
            #remove item from currentRoom
            mPlayer.currentRoom.items.remove(item)
            textwrapIMPL(f"{mPlayer.name} got {item.name}\n\n{item.description}")
            return True
            #debug:
            for i in mPlayer.currentRoom.items:
                print(i)
            for i in mPlayer.items:
                print(i)
            #debug
    textwrapIMPL(f"sorry {str} is not an item in this room")


def resolver(rawStr: str):
    if len(rawStr) == 1:
        if rawStr == "n" or rawStr == "s" or rawStr == "e" or rawStr == "w":
            moveTo(mPlayer, rawStr)
        if rawStr == "q":
            textwrapIMPL(f"Hate to see you go {mPlayer.name}, love to see you leave ;)")
            global keepPlaying
            keepPlaying = False
    elif rawStr == "help" or rawStr == "rtfm":
        print(help)
    elif len(rawStr.split(" ")) == 2:
        rawStr=rawStr.split(" ")
        if rawStr[0] == "get":
            getItem(rawStr[1])

        else:
            error()
    else:
        error()


while keepPlaying:

    #begin loop, display stuff about the current room including item loop
    textwrapIMPL(f"You are currently in {mPlayer.currentRoom.name}")
    textwrapIMPL(mPlayer.currentRoom.description)
    if mPlayer.currentRoom.items:
        textwrapIMPL("There are some things here:")
        for item in mPlayer.currentRoom.items:
            textwrapIMPL(f"~{item.name}~")

#take in user input, covert it to lower case and then send it on to resolver
    next = input("What next? Type help for options\n")
    resolver(
        next.lower())  ## arguably conversion to lowercase should be the responsibility of the resolver function, but f it i like it here

# valid user input is n s e w
#
