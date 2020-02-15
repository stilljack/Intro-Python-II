import unittest
import src.adv
from src.player import Player
from src.room import Room
from src.shared_functions import sf






class MyTestCase(unittest.TestCase):

    testRoom: Room =Room("test","testdesc")
    crashTestPlayer=Player("jack",testRoom)

    def test_something(self):
        self.assertEqual(True, True)

    def test_resolver_for_q(self):
        src.adv.resolver(self.crashTestPlayer,"q")
        self.assertEqual("Hate to see you go jack, love to see you leave ;)", sf.getLast())

    def test_resolver_n(self):
        src.adv.resolver(self.crashTestPlayer,"n")
        self.assertEqual("Sorry jack there's nowhere north to go right now", sf.getLast())

    def test_resolver_s(self):
        src.adv.resolver(self.crashTestPlayer,"s")
        self.assertEqual("Sorry jack there's nowhere south to go right now", sf.getLast())

    def test_resolver_e(self):
        src.adv.resolver(self.crashTestPlayer,"e")
        self.assertEqual("Sorry jack there's nowhere east to go right now", sf.getLast())

    def test_resolver_w(self):
        src.adv.resolver(self.crashTestPlayer,"w")
        self.assertEqual("Sorry jack there's nowhere west to go right now", sf.getLast())

if __name__ == '__main__':
    unittest.main()
