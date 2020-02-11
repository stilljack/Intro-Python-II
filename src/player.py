# Write a class to hold player information, e.g. what room they are in
# currently.
from src.room import Room


class Player:
    name:str
    currentRoom:Room

    def __init__(self, name: str, currentRoom: Room):
        self.name=name
        self.currentRoom=currentRoom
