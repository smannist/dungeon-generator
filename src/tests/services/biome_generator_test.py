import unittest
from services.biome_generator import BiomeGenerator

class TestBiomeGenerator(unittest.TestCase):
    def setUp(self):
        self.biome_generator = BiomeGenerator(30000,150,100)

    def test_biome_generator_constructor(self):
        self.assertEqual(self.biome_generator.width, 150)
        self.assertEqual(self.biome_generator.height, 100)
        self.assertEqual(self.biome_generator.steps, 30000)
        self.assertEqual(self.biome_generator.biome, [])

    def test_biome_map_is_initialized_correctly(self):
        self.biome_generator.initialize_map()
        self.assertEqual(len(self.biome_generator.biome), 150)

    def test_biome_map_is_drawn_correctly(self):
        self.biome_generator.generate_biome()
        biome = self.biome_generator.biome

        symbol_list = ["#", "."]

        for x in biome:
            for y in x:
                self.assertIn(y, symbol_list)
