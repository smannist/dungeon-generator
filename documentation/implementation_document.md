# Implementation document

## Project structure

The general idea is to separate data structures from services.

![Project structure](https://github.com/smannist/dungeon-generator/blob/main/images/dungeon_generator_project_structure.png)

- UI is the user interface class
- GenerateDungeon and GenerateBiome service classes are responsible for drawing the dungeon on a 2D matrix
- RandomWalk is responsible for providing coordinates for biome generation
- BSPTree is responsible for dividing the dungeon map into smaller sections
- BSPNode is a typical node class which contains information about coordinates and rooms

## Time complexities

The average time complexities are as follows:

- BSPTree
  - O(nlog(n))
    - n = total number of splits
- DungeonGenerator
  - O(wh)
    - w = width, h = height
- BiomeGenerator
  - O(wh+steps)
    - w = width, h = height
    - steps = number of random walk steps

More detailed explanations can be found at the testing document.

## Improvements

- One potential improvement I found would be using NumPy arrays instead of nested lists. This should lower the map generation times significantly.
  - Source: https://medium.com/@z.arderne/numpy-array-vs-nested-list-622b95d12761
