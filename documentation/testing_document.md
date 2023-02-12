# Testing document

## Unit tests

Currently tested classes:

- Room
  - Constructing a room works correctly
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

Performance tests are underway. I will be testing the performance of BSPTree data structure and the GenerateDungeon and GenerateBiome services.
Performance will most likely be visualized with matplotlib. This is going to require a little bit of coding and research, thus the testing is not finished yet.
