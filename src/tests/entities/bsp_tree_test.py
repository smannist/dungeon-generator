import unittest
from entities.bsp_tree import BSPNode, BSPTree

class TestBSPNode(unittest.TestCase):
    def setUp(self):
        self.bsp_node = BSPNode(0, 0, 10, 20)

    def test_bsp_node_constructor(self):
        self.assertEqual(self.bsp_node.width, 10)
        self.assertEqual(self.bsp_node.height, 20)
        self.assertEqual(self.bsp_node.x, 0)
        self.assertEqual(self.bsp_node.y, 0)
        self.assertIsNone(self.bsp_node.left)
        self.assertIsNone(self.bsp_node.right)
        self.assertIsNone(self.bsp_node.room)

class TestBSPTree(unittest.TestCase):
    def setUp(self):
        self.bsp_tree = BSPTree(100,150)
        self.root = self.bsp_tree.root
    
    def test_bsp_tree_constructor(self):
        self.assertIsInstance(self.root, BSPNode)
        self.assertEqual(self.bsp_tree.width, 100)
        self.assertEqual(self.bsp_tree.height, 150)
        self.assertGreater(len(self.bsp_tree.leaf_nodes), 0)

    def test_node_with_fitting_size_is_split_further(self):
        bsp_node = BSPNode(0,0,50,50)
        self.bsp_tree.split_node(bsp_node)
        self.assertIsNotNone(bsp_node.left)
        self.assertIsNotNone(bsp_node.right)
        self.assertTrue(isinstance(bsp_node.left, BSPNode) or isinstance(bsp_node.right, BSPNode))
    
    def test_node_with_too_small_size_is_not_split_further(self):
        bsp_node = BSPNode(0,0,5,5)
        self.bsp_tree.split_node(bsp_node)
        self.assertIsNone(bsp_node.left)
        self.assertIsNone(bsp_node.right)
