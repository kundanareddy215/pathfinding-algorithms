# Path Planning Algorithms

This repository contains implementations of three path planning problems using classical algorithms in Artificial Intelligence.

---

## Problem 1: Dijkstra’s Algorithm (Indian Cities)

Dijkstra’s Algorithm is implemented to compute the shortest path between cities in India using road distances.

* Cities are represented as nodes
* Roads are represented as weighted edges
* Distances are taken from an open-source style dataset (CSV)

### Features

* Graph constructed from external data (CSV file)
* Computes shortest distance from a source city to all other cities
* Demonstrates Uniform Cost Search

---

## Problem 2: UGV Navigation with Static Obstacles

This problem simulates an Unmanned Ground Vehicle (UGV) navigating a grid-based battlefield with static obstacles.

### Approach

* The environment is represented as a grid
* Obstacles are randomly generated
* The A* search algorithm is used to find the shortest path

### Features

* Grid-based path planning
* Random obstacle generation
* Tested with different obstacle densities:

  * Low density
  * Medium density
  * High density

---

## Problem 3: UGV Navigation with Dynamic Obstacles

This problem extends Problem 2 by introducing dynamic obstacles that appear after the initial path is computed.

### Approach

* Initial path is computed using A*
* Environment changes dynamically (new obstacle added)
* Path is recomputed to adapt to the new environment

### Features

* Dynamic replanning
* Demonstrates real-world adaptability of path planning algorithms
* Handles cases where no path exists

---

## Algorithms Used

* Dijkstra’s Algorithm (Uniform Cost Search)
* A* Search Algorithm



