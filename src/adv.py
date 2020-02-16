import os
from src.shared_functions import sf
from src.item import *
from src.room import *
from src.help import *
from src.player import *



# set out keep playing variable to true to figure out of we need to play another turn or not
keepPlaying = True

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


def quitGame(target: Player):
    sf.textwrapIMPL(f"Hate to see you go {target.name}, love to see you leave ;)")
    global keepPlaying
    keepPlaying = False
    if __name__ == '__main__':
        os._exit(31337)


def error():
    sf.textwrapIMPL("Invalid entry, sorry, please type help to RTFM")

def getItem(target: Player, str):
    for item in target.currentRoom.items:
        if str in listOfItems and item == listOfItems[str]:
            # ADD ITEM TO PLAYERS LIST
            target.items.append(item)
            # remove item from currentRoom
            target.currentRoom.items.remove(item)
            sf.textwrapIMPL(f"{target.name} got {item.name}\n\n{item.description}")
            return True
    sf.textwrapIMPL(
        f"sorry {str} is not an item in this room (maybe you want to type drop itemname to discard it from your person?)")


def dropItem(target: Player, str):
    for item in target.items:
        if str in listOfItems and item == listOfItems[str]:
            # remove ITEM froms PLAYERS LIST
            target.items.remove(item)
            # add item to currentRoom
            target.currentRoom.items.append(item)
            sf.textwrapIMPL(f"{target.name} dropped {item.name}")
            return True
    sf.textwrapIMPL(
        f"sorry {str} is not an item you have on your person (maybe you want to type get itemname to pick up off the floor?)")


def resolver(target: Player, rawStr: str):
    if len(rawStr) == 1:
        if rawStr in ("n", "s", "e", "w"):
            target.moveTo(rawStr)
        if rawStr == "q":
            quitGame(target)
    elif rawStr == "help" or rawStr == "rtfm":
        print(help)
    elif len(rawStr.split(" ")) == 2:
        rawStr = rawStr.split(" ")
        # print (f"rawstr 0 = {rawStr[0]} \n and rawstr 1 = {rawStr[1]}")
        if rawStr[0] in ("get", "take"):
            getItem(target, rawStr[1])
        if rawStr[0] == "drop":
            dropItem(target, rawStr[1])
    else:
        error()


def checkFormat(str: str):
    # if you do have an alphanumeric string, lowcase it and send it on to the resolver
    if str.isalpha():
        return str.lower()
    if len(str.split(" ")) >= 2:
        split = str.split(" ")
        # if there's non alphanumerics, we should dump the user input
        for i in split:
            if not i.isalpha():
                sf.textwrapIMPL(
                    "Your Input is whackadoodle, please try entering something reasonable or type help for some help!")
                return "Blank"
        return str.lower()
    else:
        sf.textwrapIMPL(
            "Your Input is whackadoodle, please try entering something reasonable or type help for some help!")
        return "blank"


def adventureTime():
    global keepPlaying
    print("Adventure game or whatever!")

    mPlayer = Player(
        name=input("enter your name:"),
        currentRoom=listOfRooms['outside']
    )

    # welcome player
    print(f"Hello {mPlayer.name}! lets get to getting")

    while keepPlaying:

        # begin loop, display stuff about the current room including item loop
        sf.textwrapIMPL(f"You are currently in {mPlayer.currentRoom.name}")
        sf.textwrapIMPL(mPlayer.currentRoom.description)
        if mPlayer.currentRoom.items:
            sf.textwrapIMPL("There are some things here:")
            for item in mPlayer.currentRoom.items:
                sf.textwrapIMPL(f"~{item.name}~")

        # take in user input, check for sanity and sanitize it, then send it on to resolver
        next = checkFormat(input("What next? Type help for options\n"))
        resolver(
            mPlayer,
            next
        )  ## arguably conversion to lowercase should be the responsibility of the resolver function, but f it i like it here


# valid user input is n s e w
#
if __name__ == '__main__':
    adventureTime()
