# Introduction to the Game Of Life

The game of life is a **cellular automaton** created by mathematician John Horton Conway in 1970

What is a cellular automaton? It is apparently a discrete system of cells that evolve according to rules based on neighboring states

# #Why do I want to create a simulation of the Game of Life

Idk. Looks cool and I watched a Veritasium Video about it

#Rules

## Structure

The board that the Game of Life is played on is a "infinite, two-dimensional grid of square cells"

Each cell in the grid has 2 possible states, live or dead.
Each cell interacts with 8 neighbors

## Generational Rule

1. Any live cell with <2 live neighbours dies.
2. Any live cell with 2 or 3 neighbors lives to next generation
3. Any live cell with more than 3 live neighbours dies
4. Any dead call can revive if there are exactly 3 live neighbours.

The game of life begins when the first initial pattern is created and the rules applies, creating the next generation
