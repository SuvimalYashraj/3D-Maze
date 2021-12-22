# 3D MAZE

## Overview
Apply AI search techniques to lead an exploration team to explore an underground cave system.
Each cave system is like a sophisticated 3D maze, which consists of a grid of points with (x, y, z) locations in which your agent may use one of the 18 elementary actions, named X+, X-, Y+, Y-, Z+, Z-;X+Y+, X-Y+, X+Y-, X-Y-, X+Z+, X+Z-, X-Z+, X-Z-, Y+Z+, Y+Z-, Y-Z+, Y-Z-; to move to one of the 18 neighboring grid point locations.
At each grid point, your agent is given a list of actions that are available for the current point your agent is at. Your agent can select and execute  one of these available actions to move inside the 3D maze.

## Objective
Find the optimal path from the initial entrance grid location to the exit grid location. A path is composed of a sequence of legal moves. Each legal move consists of moving the agent from a point to one of its 18 neighbor points, using one of the elementary actions that are available at
the current location.

## Algorithms 
- Breadth-first search (BFS)
- Uniform-cost search (UCS)
- A* search (A*)
