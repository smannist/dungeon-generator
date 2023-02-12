import unittest
from services.random_walk import RandomWalk

class TestRandomWalk(unittest.TestCase):
    def setUp(self):
        self.random_walk = RandomWalk(1000,150,100)

    def test_random_walk_constructor_is_valid(self):
        self.assertEqual(self.random_walk.x, 75)
        self.assertEqual(self.random_walk.y, 50)
        self.assertEqual(self.random_walk.width, 150)
        self.assertEqual(self.random_walk.height, 100)
        self.assertEqual(self.random_walk.steps, 1000)
        self.assertEqual(self.random_walk.step_count, 0)
        self.assertEqual(self.random_walk.walk_coordinates, [])

    def test_size_of_walk_coordinates_list_is_equal_to_number_of_steps_taken(self):
        self.random_walk.walk_randomly()
        walk_coordinates = self.random_walk.walk_coordinates
        self.assertEqual(len(walk_coordinates), 1000)

    def test_all_walk_coordinates_are_with_the_boundaries_of_the_map(self):
        self.random_walk.walk_randomly()
        walk_coordinates = self.random_walk.walk_coordinates
        
        for step in walk_coordinates:
            self.assertTrue(0 <= step[0] < self.random_walk.width)
            self.assertTrue(0 <= step[1] < self.random_walk.height)
