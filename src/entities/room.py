

class Room:
    """A class containing the information of a single room
    Args:
        x (int): x-coordinate
        y (int): y-coordinate
        height (int): room height
        width (int): room width
    """
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.xy = x+width
        self.yx = y+height
        self.height = height
        self.width = width

    @property
    def center(self):
        """ Returns the center of the room
        Returns:
            tuple: (x, y) center coordinates of the room
        """
        x = self.x + self.width // 2
        y = self.y + self.height // 2
        return x, y
