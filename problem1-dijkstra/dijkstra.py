import heapq

def dijkstra(graph, start):

    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:

        current_distance, current_city = heapq.heappop(pq)

        for neighbor, weight in graph[current_city]:

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


graph = {
    "Hyderabad": [("Bangalore", 570), ("Chennai", 630)],
    "Bangalore": [("Hyderabad", 570), ("Chennai", 350)],
    "Chennai": [("Hyderabad", 630), ("Bangalore", 350)]
}

start_city = "Hyderabad"

result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)

for city in result:
    print(city, ":", result[city], "km")
