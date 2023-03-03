import unittest
from services.dungeon_generator import DungeonGenerator
from entities.bsp_tree import BSPTree, BSPNode

class TestDungeonGenerator(unittest.TestCase):
    def setUp(self):
        self.bsp_tree = BSPTree(200,150)
        self.dungeon_generator = DungeonGenerator(self.bsp_tree, 60, 90)

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

    def test_rooms_are_within_boundaries_of_the_map(self):
        #the rooms should always be within boundaries of the map since
        #bsp tree works by splitting the whole map into smaller pieces
        #which are always smaller than the original map
        #but i included the test for clarity anyway
        leaf_nodes = self.bsp_tree.leaf_nodes
        self.dungeon_generator.generate_dungeon()

        for node in leaf_nodes:
            if node.room is not None:
                self.assertTrue(0 <= node.room.width <= self.bsp_tree.width)
                self.assertTrue(0 <= node.room.height <= self.bsp_tree.height)
