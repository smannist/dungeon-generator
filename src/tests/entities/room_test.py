import unittest
from entities.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5,5,20,20)

    def test_room_constructor(self):
        self.assertEqual(self.room.x,5)
        self.assertEqual(self.room.y,5)
        self.assertEqual(self.room.height,20)
        self.assertEqual(self.room.width,20)
        self.assertEqual(self.room.xy,5+20)
        self.assertEqual(self.room.yx,5+20)
