# User guide

## Installation

1. Open terminal and clone the repository on your system with the command:

```bash
git clone https://github.com/smannist/dungeon-generator.git
```

2. Install Poetry by following the instructions on their [website](https://python-poetry.org/docs/)

3. After installing Poetry, you'll need to install the required dependencies by running the following command:

```bash
poetry install
```

4. Finally to run the program type:

```bash
poetry run invoke start
```

## Using the application

Using the application is fairly simple. To generate a dungeon choose desired minimum and maximum size of the rooms and simply hit "generate dungeon" button:

![Generating a dungeon](https://github.com/smannist/dungeon-generator/blob/main/images/user_guide_1.png)

To generate a biome just choose the number of random walk steps and hit the "generate biome" button:

![Generating a biome](https://github.com/smannist/dungeon-generator/blob/main/images/user_guide_2.png)

If you want to run tests run the command:

```bash
poetry run invoke test
```

If you want to generate coverage report run the command:

```bash
poetry run invoke coverage
```

And to view the coverage report on your browser (on Linux systems) run the command:

```bash
poetry run invoke report
```
