import heapq
import csv

def load_graph_from_csv(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            c1 = row['city1']
            c2 = row['city2']
            dist = int(row['distance'])

            if c1 not in graph:
                graph[c1] = []
            if c2 not in graph:
                graph[c2] = []

            graph[c1].append((c2, dist))
            graph[c2].append((c1, dist))  # undirected graph

    return graph


def dijkstra(graph, start):

    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:

        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city]:

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# LOAD DATA FROM CSV (OPEN SOURCE STYLE)
graph = load_graph_from_csv("india_cities.csv")

start_city = "Delhi"

result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)

for city in result:
    print(city, ":", result[city], "km")
