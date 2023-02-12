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

- TODO

## Improvements

- TODO
