import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:
            return g_cost[current]

        for d in directions:

            nx = current[0] + d[0]
            ny = current[1] + d[1]

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:

                new_cost = g_cost[current] + 1

                if (nx,ny) not in g_cost or new_cost < g_cost[(nx,ny)]:

                    g_cost[(nx,ny)] = new_cost
                    priority = new_cost + heuristic((nx,ny), goal)

                    heapq.heappush(open_list,(priority,(nx,ny)))

    return None


grid = [
[0,0,0,1,0],
[0,1,0,1,0],
[0,0,0,0,0],
[1,0,1,0,0],
[0,0,0,0,0]
]

start = (0,0)
goal = (4,4)

distance = astar(grid,start,goal)

print("Shortest path length:", distance)
