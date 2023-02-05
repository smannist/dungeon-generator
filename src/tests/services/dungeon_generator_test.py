import unittest
from services.dungeon_generator import DungeonGenerator
from entities.bsp_tree import BSPTree, BSPNode

class TestDungeonGenerator(unittest.TestCase):
    def setUp(self):
        self.bsp_tree = BSPTree(200,150)
        self.dungeon_generator = DungeonGenerator(self.bsp_tree)

    def test_dungeon_is_created_with_correct_dimensions(self):
        self.dungeon_generator.initialize_map()
        self.assertEqual(len(self.dungeon_generator.dungeon), 200)

    def test_dungeon_is_generated(self):
        dungeon = self.dungeon_generator.generate_dungeon()
        self.assertIsNot(dungeon, [])

    def test_neighbors_and_costs_are_returned_correctly(self):
        node = BSPNode(1,3,0,0)
        leaf_nodes = [BSPNode(5,10,0,0), BSPNode(11,34,0,0)]
        neighbors = self.dungeon_generator.get_neighbors(node,leaf_nodes)
        self.assertEqual(neighbors, [(30,leaf_nodes[0]), (0,leaf_nodes[1])])

    def test_no_neighbors_are_found_if_distance_is_too_great(self):
        node = BSPNode(1,3,0,0)
        leaf_nodes = [BSPNode(100,100,0,0)]
        neighbors = self.dungeon_generator.get_neighbors(node,leaf_nodes)
        self.assertEqual(neighbors, [])
