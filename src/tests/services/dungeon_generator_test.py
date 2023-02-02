import unittest
from services.dungeon_generator import DungeonGenerator
from entities.bsp_tree import BSPTree

class TestDungeonGenerator(unittest.TestCase):
    def setUp(self):
        self.bsp_tree = BSPTree(200,150)
        self.dungeon_generator = DungeonGenerator(self.bsp_tree)

    def test_dungeon_is_created_with_correct_dimensions(self):
        self.dungeon_generator.initialize_map()
        self.assertEqual(len(self.dungeon_generator.dungeon), 200)
