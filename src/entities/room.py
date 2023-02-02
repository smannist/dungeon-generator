

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
