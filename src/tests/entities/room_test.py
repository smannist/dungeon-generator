import unittest
from entities.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5,5,20,20)