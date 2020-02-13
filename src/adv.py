
from src.shared_functions import *
from src.item import *
from src.room import *
from src.help import *
from src.player import *




#
# Main
#
# Make a new player object that is currently in the 'outside' room.

print("Adventure game or whatever!")

mPlayer = Player(
    name=input("enter your name:"),
    currentRoom=listOfRooms['outside']
)





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
    textwrapIMPL(f"sorry {str} is not an item in this room (maybe you want to type drop itemname to discard it from your person?)")

def dropItem(str):
    for item in mPlayer.items:
        if str in listOfItems and item == listOfItems[str]:
            #remove ITEM froms PLAYERS LIST
            mPlayer.items.remove(item)
            #add item to currentRoom
            mPlayer.currentRoom.items.append(item)
            textwrapIMPL(f"{mPlayer.name} dropped {item.name}")
            return True
    textwrapIMPL(f"sorry {str} is not an item you have on your person (maybe you want to type get itemname to pick up off the floor?)")


def resolver(rawStr: str):
    if len(rawStr) == 1:
        if rawStr in ("n","s","e","w"):
            mPlayer.moveTo(rawStr)
        if rawStr in "nsew":
            print(f"triggered for {rawStr}")
            mPlayer.moveTo(rawStr)
        if rawStr == "q":
            textwrapIMPL(f"Hate to see you go {mPlayer.name}, love to see you leave ;)")
            global keepPlaying
            keepPlaying = False
    elif rawStr == "help" or rawStr == "rtfm":
        print(help)
    elif len(rawStr.split(" ")) == 2:
        rawStr=rawStr.split(" ")
        print (f"rawstr 0 = {rawStr[0]} \n and rawstr 1 = {rawStr[1]}")
        if rawStr[0] in ("get", "take"):
            getItem(rawStr[1])
        if rawStr[0] == "drop":
            dropItem(rawStr[1])

    else:
        print("end debug 2")
        error()

def checkFormat(str:str):
    #if you do have an alphanumeric string, lowcase it and send it on to the resolver
    if str.isalpha():
        return str.lower()
    else:
        textwrapIMPL("Your Input is whackadoodle, please try entering something reasonable or type help for some help!")
        return "blank"

while keepPlaying:

    #begin loop, display stuff about the current room including item loop
    textwrapIMPL(f"You are currently in {mPlayer.currentRoom.name}")
    textwrapIMPL(mPlayer.currentRoom.description)
    if mPlayer.currentRoom.items:
        textwrapIMPL("There are some things here:")
        for item in mPlayer.currentRoom.items:
            textwrapIMPL(f"~{item.name}~")

#take in user input, check for sanity and sanitize it, then send it on to resolver
    next = checkFormat(input("What next? Type help for options\n"))
    resolver(
        next
    )## arguably conversion to lowercase should be the responsibility of the resolver function, but f it i like it here


# valid user input is n s e w
#
