# Testing document

## Unit tests

Currently tested classes:

- Room
  - Constructing a room works correctly
- BSPTree
  - Constructor tests
  - Node with correct dimensions is split further
  - Node with incorrect dimensions is not split further
  - Node with height/width ration > 1.6 is split vertically
  - Node with width/height ratio > 1.3 is split horizontally
- Dungeon generator class
  - Dungeon map is initialized with correct dimensions
  - Dungeon map is generated and it is not empty
- Biome generator class
  - Constructor tests
  - Biome map is initialized with correct dimensions
  - Biome map is generated and not empty
  - Biome map is generated correctly, consisting only of correct symbols "#" and "."
- Random walk class
  - Constructor tests
  - Walk coordinates list is created with correct number of steps
  - Coordinates are within boundaries of the initialized map
  - Right, left, up and down steps are working as expected
  - Valid steps are accepted
  - Invalid steps outside of map boundaries are not accepted
- UI will not be tested

Current coverage:

![Coverage](https://github.com/smannist/dungeon-generator/blob/main/images/coverage_2.png)

## Performance tests

The time complexities are all average cases. In worst-case scenarios the algorithms will run longer.

BSPTree:

- The most taxing part is the split_node function which recursively splits the given area into smaller pieces until the threshold is reached
  - N number of splits are required to reach the threshold thus the time complexity is O(n)
- The rest of the operations and helper functions run in constant time O(1)
- Thus on average the algorithm runs in a linear time O(n)

![Performance BSPTree](https://github.com/smannist/dungeon-generator/blob/main/images/BSPTREE_performance_test.png)
