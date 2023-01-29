import unittest
from services.dungeon_generator import DungeonGenerator

class TestDungeonGenerator(unittest.TestCase):
    def setUp(self):
        self.map = DungeonGenerator(5, 20, 20, 50)

    def test_map_is_created_with_correct_dimensions(self):
        map = self.map.initialize()
        self.assertEqual(len(map), 20*50)
