import random

MINIMUM_LEAF_SIZE = 15
MINIMUM_SPACE = -5

class BSPNode:
    """ A Class for holding a single node of the BSP Tree. Contains positions and room info.
    Args:
        x (int): x-coordinate of the area
        y (int): y-coordinate of the area
        width (int): width of the split area
        height: height of the split area
    """
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.room = None

class BSPTree:
    """ A Class for holding the BSP Tree
    Args:
        width (int): max width of the area
        height (int): max height of the area
    """
    def __init__(self, width, height):
        self.root = BSPNode(2, 0, width, height)
        self.width = width
        self.height = height
        self.leaf_nodes = []

        self.split_node(self.root)

    def split_node(self, node):
        """ Method for splitting the node. Determines split size and direction.
        """
        if node.left is not None or node.right is not None:
            return False

        split_vertically = self.determine_split_axis(node)
        max_split_size = self.get_max_split(node, split_vertically)

        if max_split_size <= MINIMUM_LEAF_SIZE:
            self.leaf_nodes.append(node)
            return False

        split = self.get_split_size(MINIMUM_LEAF_SIZE, max_split_size)

        self.create_children(node, split, split_vertically)

        self.split_node(node.right)
        self.split_node(node.left)

        return True

    def determine_split_axis(self, node):
        """ Method for determinating the split axis
        Returns:
            bool: True / False based on dimensions, else random
        """

        if node.width == 0 or node.height == 0:
            return False

        if node.width/node.height >= 1.3:
            return False

        if node.height/node.width >= 1.6:
            return True

        return random.choice([True, False])

    def get_max_split(self, node, split_vertically):
        """ Method for determinating max split size
        Returns:
            int: Maximum split size
        """
        return node.height - MINIMUM_LEAF_SIZE if split_vertically else node.width - MINIMUM_LEAF_SIZE

    def get_split_size(self, min_split, max_split):
        """ Method for determining the split size
        Returns:
            int: Size of split area
        """
        split = random.randint(min_split, max_split)
        split = split + MINIMUM_SPACE if split + MINIMUM_SPACE < max_split else max_split
        return split

    def create_children(self, node, split, split_vertically):
        """ Method for creating children of the given node
        """
        if split_vertically:
            node.right = BSPNode(node.x, node.y+1, node.width, split)
            node.left = BSPNode(node.x, node.y + split, node.width, \
                                node.height - split)
        else:
            node.right = BSPNode(node.x, node.y, split, node.height)
            node.left = BSPNode(node.x + split, node.y, node.width-split, \
                                node.height)
