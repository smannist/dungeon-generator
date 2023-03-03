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
  - Test that rooms are within boundaries of the map (due to the nature of bsp tree this is not really necessary, but I added the test for clarity)
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

## Coverage

![Coverage](https://github.com/smannist/dungeon-generator/blob/main/images/coverage_2.png)

## Performance tests

The time complexities are all average cases. In worst-case scenarios the algorithms will run longer. Randomization also adds plenty of factors.

BSPTree:

- It takes n number of iterations to reach the max threshold for split areas
  - Children for the nodes are created each split. This takes log(n) time.
- Hence, in total the time complexity is around O(nlog(n))

![Performance BSPTree](https://github.com/smannist/dungeon-generator/blob/main/images/BSPTREE_performance_test.png)

DungeonGenerator:

- The most taxing functions are initializing the map and creating rooms.
  - This takes O(wh) time where w = width of the map and h = height of the map
- Hence the time complexity is O(wh)

![Performance GenerateDungeon](https://github.com/smannist/dungeon-generator/blob/main/images/GenerateDungeon_performance_test.png)

BiomeGenerator:

- Similarly to DungeonGenerator, the most taxing function is initializing the map.
  - Same time complexity, O(wh)
- Constructor initializes the random walk, this takes O(steps) time
- Hence the time complexity is O(wh+steps)
- Although the time complexity is similar to DungeonGenerator the performance is a lot better since
  the BSPTtree is not required, creation of rooms is not required etc.

![Performance BiomeGenerator](https://github.com/smannist/dungeon-generator/blob/main/images/GenerateBiome_performance_test.png)
