import math


def find_solution(edges):

    neighbors = {}
    visited = set()
    smallest_size = math.inf
    largest_size = 2

    for edge in edges:
        if edge[0] not in neighbors:
            neighbors[edge[0]] = []
        if edge[1] not in neighbors:
            neighbors[edge[1]] = []

        neighbors[edge[0]].append(edge[1])
        neighbors[edge[1]].append(edge[0])

    for node in neighbors.keys():
        if node not in visited:
            current_size, visited = DFS(node, neighbors, visited, node_count=0)

            if current_size <= smallest_size:
                smallest_size = current_size
            if current_size >= largest_size:
                largest_size = current_size

    print(str(smallest_size)+" "+str(largest_size))


def DFS(node, neighbors, visited, node_count):
    list = []
    list.append(node)

    while len(list)>0:
        node = list.pop()
        if node not in visited:
            visited.add(node)
            node_count += 1
            for neighbor in neighbors[node]:
                list.append(neighbor)

    return node_count, visited


if __name__ == "__main__":
    q = int(input().strip())
    edges = []
    for line in range(q):
        edges.append([int(edge) for edge in input().strip().split(" ")])

    find_solution(edges)