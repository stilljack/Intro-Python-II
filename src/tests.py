import unittest

import src.adv
from src.player import Player
from src.room import Room
from src.shared_functions import *
import sys

# read whatever output the previous script piped here
# but only keep the last line (stripping the newline...)


class TestADV(unittest.TestCase):

    testRoom: Room =Room("test","testdesc")
    crashTestPlayer=Player("jack",testRoom)

    def main(self):

         def resolverTestError(self):
             src.adv.resolver("nonsense")
             for line in sys.stdin:
                tmp = line.strip()
                print(tmp)

             self.assertEqual("Hate to see you go jack, love to see you leave ;)", stringtestingholder, "Should be 6")

    if __name__ == '__main__':
         unittest.main()
