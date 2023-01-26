
GRAY = (169,169,169)

class Room:

    """Entity containing the information of a single room
    Args:
        row (int): Coordinates of the row
        col (int): Coordinates of the column
        height (int): Height of the room
        width (int): Width of the room
    """

    def __init__(self,row,col,height,width):
        self.color = GRAY
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.height = height
        self.width = width