import sys


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Complete this function
    city_dict = {}
    visited = set()
    connected_components = 0
    roads = 0

    for i in range(1,n+1):
         city_dict[i] = []

    for edge in cities:
        city_dict[edge[0]].append(edge[1])
        city_dict[edge[1]].append(edge[0])

    for i in range(1, n+1):
        if i not in visited:
            connected_components += 1
            roads += DFS(i, visited, city_dict, road_count = 0) - 1

    cost1 = c_road*roads + connected_components* c_lib
    cost2 = n*c_lib

    return min(cost1, cost2)


def DFS(i, visited, city_dict, road_count):
    neighbors = city_dict[i]
    visited.add(i)
    road_count += 1

    for neighbor in neighbors:
        if neighbor not in visited:
            road_count = DFS(neighbor, visited, city_dict, road_count)

    return road_count





if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
           cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
