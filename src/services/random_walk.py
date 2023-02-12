import random

class RandomWalk:
    """Class for random walk algorithm
    Args:
        steps (int): number of steps taken
        width (int): width of the map
        height (int): height of the map
    """
    def __init__(self,steps,width,height):
        self.x = width // 2
        self.y = height // 2
        self.width = width
        self.height = height
        self.steps = steps
        self.step_count = 0
        self.walk_coordinates = []

    def walk_randomly(self):
        """ Method for randomly choosing the taken steps.
            Appends the steps into a list.
        """
        for _ in range(self.steps):
            randomize_step = random.random()

            if randomize_step <= 0.25:
                self.left_step()
            elif randomize_step <= 0.5:
                self.right_step()
            elif randomize_step <= 0.75:
                self.up_step()
            else:
                self.down_step()

            self.walk_coordinates.append((self.x, self.y))

    def right_step(self):
        """ Method for moving right on the map
        Returns:
            int: step direction
        """
        self.x = self.x + 1
        if self.validate_step(self.x, self.y):
            return self.step_count + 1
        return 0

    def left_step(self):
        """ Method for moving left on the map
        Returns:
            int: step direction
        """
        self.x = self.x - 1
        if self.validate_step(self.x, self.y):
            return self.step_count + 1
        return 0

    def up_step(self):
        """ Method for moving up on the map
        Returns:
            int: step direction
        """
        self.y = self.y - 1
        if self.validate_step(self.x, self.y):
            return self.step_count + 1
        return 0

    def down_step(self):
        """ Method for moving down on the map
        Returns:
            int: step direction
        """
        self.y = self.y + 1
        if self.validate_step(self.x, self.y):
            return self.step_count + 1
        return 0

    def validate_step(self,step_x,step_y):
        """ A method for checking that the a given step is valid
        Returns:
            bool: True if step is valid, False if not
        """
        if step_x < 0 or step_x >= self.width or step_x <= self.width:
            return False

        if step_y < 0 or step_y >= self.height or step_y <= self.height:
            return False

        return True

    def get_walk_coordinates(self):
        """ Method for returning list of steps taken
        Return:
            list: full random walk coordinates as a list of steps
        """
        return self.walk_coordinates
