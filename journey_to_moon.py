import sys


def journeyToMoon(n, astronaut):
    # Complete this function

    graph ={}
    visited = set()

    for i in range(n):
        graph[i] = []

    for edge in astronaut:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    size_list = []
    for node in graph:
        if node not in visited:
            size, visited = DFS(node, graph, visited, size = 0)
            size_list.append(size)

    sum = 0
    answer = 0
    for counts in size_list:
        answer += sum * counts
        sum += counts

    return answer

def DFS(node, graph, visited, size):
    list = []
    list.append(node)

    while len(list)>0:
        node = list.pop()
        if node not in visited:
            visited.add(node)
            size += 1
            for neighbor in graph[node]:
                list.append(neighbor)

    return size, visited






if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
       astronaut_t = [int(astronaut_temp) for astronaut_temp in input().strip().split(' ')]
       astronaut.append(astronaut_t)
    result = journeyToMoon(n, astronaut)
    print(result)