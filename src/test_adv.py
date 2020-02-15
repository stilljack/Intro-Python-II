import unittest
import src.adv
from src.player import Player
from src.room import Room
from src.shared_functions import shared_func
from src.adv import sf


testRoom: Room =Room("test","testdesc")
crashTestPlayer=Player("jack",testRoom)



class MyTestCase(unittest.TestCase):



    def test_something(self):
        self.assertEqual(True, True)

    def test_resolver(self):

        src.adv.resolver(crashTestPlayer,"q")
        self.assertEqual("Hate to see you go jack, love to see you leave ;)", sf.getLast())


if __name__ == '__main__':
    unittest.main()
