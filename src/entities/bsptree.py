import random

class BSPNode:
    """ A single node of a BSPTree which stores information about coordinates and room
    Args:
        x (int): x-coordinate
        y (int): y-coordinate
        width (int): total width
        height (int): total height
    """
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left_child = None
        self.right_child = None
        self.room = None

class BSPTree:
    """ A class for holding the BSP Tree
    Args:
        coordinate_list (list): list of coordinates
    """
    def __init__(self, coordinate_list):
        self.root = self.split(coordinate_list)

    def get_root(self):
        return self.root

    def split(self, coordinate_list):
        """ Recursively create a randomized BSP tree with node splitting using
            x-coordinates as the decider
        Args:
            coordinate_list (list): list of coordinates
        Returns:
            node (BSPNode): next node
        """
        if len(coordinate_list) == 0:
            return None

        randomize = random.randint(0, len(coordinate_list)-1)
        split_point = coordinate_list.pop(randomize)

        left_children = []
        right_children = []

        for node in coordinate_list:
            if node[0] < split_point[0]:
                left_children.append(node)
            if node[0] >= split_point[0]:
                right_children.append(node)

        node = BSPNode(split_point[0],split_point[1],split_point[2],split_point[3])

        node.left_child = self.split(left_children)
        node.right_child = self.split(right_children)

        return node

    def print_tree(self, node):
        """ Prints the tree
        Args:
            node (BSPNode): root node
        """
        if node is None:
            return None
        print(node.x, node.y, node.width, node.height)
        self.print_tree(node.left_child)
        self.print_tree(node.right_child)

if __name__ == "__main__":
    coordinate_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [92,23,13,42], [10,10,12,23]]
    bsp_tree = BSPTree(coordinate_list)
    bsp_tree.print_tree(bsp_tree.root)
