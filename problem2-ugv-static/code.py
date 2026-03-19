import heapq
import random


# Heuristic (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Algorithm
def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:
            return g_cost[current]

        for d in directions:

            nx = current[0] + d[0]
            ny = current[1] + d[1]

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:

                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)

                    heapq.heappush(open_list, (priority, (nx, ny)))

    return None


# Generate grid with random obstacles
def generate_grid(size, obstacle_prob):

    grid = []

    for i in range(size):
        row = []
        for j in range(size):

            if random.random() < obstacle_prob:
                row.append(1)   # obstacle
            else:
                row.append(0)   # free

        grid.append(row)

    return grid


# MAIN PROGRAM

size = 10   # scaled version of 70x70
start = (0, 0)
goal = (size - 1, size - 1)


# LOW density
grid_low = generate_grid(size, 0.1)
grid_low[0][0] = 0
grid_low[size-1][size-1] = 0

# MEDIUM density
grid_medium = generate_grid(size, 0.2)
grid_medium[0][0] = 0
grid_medium[size-1][size-1] = 0

# HIGH density
grid_high = generate_grid(size, 0.3)
grid_high[0][0] = 0
grid_high[size-1][size-1] = 0


print("Low density:", astar(grid_low, start, goal))
print("Medium density:", astar(grid_medium, start, goal))
print("High density:", astar(grid_high, start, goal))
