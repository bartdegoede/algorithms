graph = {
    'E': ['C', 'G'],
    'C': ['B', 'D'],
    'G': ['H'],
    'B': [],
    'D': ['H'],
    'H': []
}

visited = set()
queue = []

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    print('Start visiting everything at E')
    bfs(visited, graph, 'E')
