import unittest
from services.dungeon_generator import DungeonGenerator
from entities.bsp_tree import BSPTree, BSPNode

class TestDungeonGenerator(unittest.TestCase):
    def setUp(self):
        self.bsp_tree = BSPTree(200,150)
        self.dungeon_generator = DungeonGenerator(self.bsp_tree)

    def test_dungeon_generator_constructor(self):
        self.assertIsInstance(self.dungeon_generator.bsp_tree, BSPTree)
        self.assertIsInstance(self.dungeon_generator.root, BSPNode)
        self.assertEqual(self.dungeon_generator.width, 200)
        self.assertEqual(self.dungeon_generator.height, 150)
        self.assertGreater(len(self.dungeon_generator.leaf_nodes), 0)
        self.assertEqual(self.dungeon_generator.dungeon, [])

    def test_dungeon_is_created_with_correct_dimensions(self):
        self.dungeon_generator.initialize_map()
        self.assertEqual(len(self.dungeon_generator.dungeon), 200)

    def test_dungeon_is_generated(self):
        dungeon = self.dungeon_generator.generate_dungeon()
        self.assertIsNot(dungeon, [])
