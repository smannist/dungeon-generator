# Project specification

## Introduction

The project is part of Bachelor's Programme in Computer Science. English will be used for both documentation and programming (function/method names etc.)

## Problem to be solved

The goal is to demonstrate different algorithmic implementations for procedural dungeon generation. For example:

- Generating more dungeon-esque maps with BSP + Astar algorithm
- Creating more forestry / deserty biomes using the random walk algorithm.

Users will be able to adjust the generation parameters, such as room and map size. Pygame library will be used for visualization.

## Programming language

Python will be used for this project. However, I am also familiar with both Java and JavaScript, so if necessary, I can peer review projects written in those languages as well.

## Data structures and algorithms

At least the following data structures:

- Tree (BSP)
- Array(s)
- Dictionary

Algorithms:

- BSP for square dungeon-like areas with random size rooms.
- A\* for connecting the rooms with pathways.
- Random walk to represent more cave/forest/desert-like biome areas.

Time complexity:

- Worst-case for A\* should be O(b^d) where b is the branching factor and d is the depth of the graph (tree).
- Random walk should be around O(nlogn)

Time complexities are just estimations. It's difficult to make accurate predictions this early, accurate time complexities will be included as the project evolves.

## Inputs

At the very least:

- Minimum and maximum size of the rooms.
- Minimum and maximum size of the map.
- Number of iterations for random walk generated maps.

The final application will most likely feature more inputs.

## Conclusion

In this document, I have presented a project specification for procedual dungeon generation using BSP, A\* and Random Walk algorithms. The project will be implemented in Python, and it will allow the user to adjust parameters such as room and map size. The final application will be able to visualize the generated dungeons using the Pygame library.

## Sources

1. Dungeon generation using BSP trees (2013). https://eskerda.com/bsp-dungeon-generation/
2. Generating Semi-Natural Landmasses using a Random Walk. https://www.reddit.com/r/Python/comments/q2h5og/generating_seminatural_landmasses_using_a_random/
3. A* search algorithm. Wikipedia. https://en.wikipedia.org/wiki/A*\_search_algorithm
