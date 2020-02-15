# Write a class to hold player information, e.g. what room they are in
# currently.
from src.room import Room
from src.shared_functions import sf

class Player:
    name: str
    currentRoom: Room
    items = []

    def __init__(self, name: str, currentRoom: Room):
        self.name = name
        self.currentRoom = currentRoom

    def moveTo(self, letter: str):
        if letter == "n":
            if self.currentRoom.n_to == "":
                sf.textwrapIMPL(f"Sorry {self.name} there's nowhere north to go right now")
            else:
                self.currentRoom = self.currentRoom.n_to
        if letter == "s":
            if self.currentRoom.s_to == "":
                sf.textwrapIMPL(f"Sorry {self.name} there's nowhere south to go right now")
            else:
                self.currentRoom = self.currentRoom.s_to
        if letter == "w":
            if self.currentRoom.w_to == "":
                sf.textwrapIMPL(f"Sorry {self.name} there's nowhere west to go right now")
            else:
                self.currentRoom = self.currentRoom.w_to
        if letter == "e":
            if self.currentRoom.e_to == "":
                sf.textwrapIMPL(f"Sorry {self.name} there's nowhere east to go right now")
            else:
                self.currentRoom = self.currentRoom.e_to


