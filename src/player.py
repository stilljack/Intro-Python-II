# Write a class to hold player information, e.g. what room they are in
# currently.
from src.room import Room


class Player:
    name=""
    currentRoom:Room

    def __init__(self, name: str, room: Room):
        self.name=name
        self.room=room
