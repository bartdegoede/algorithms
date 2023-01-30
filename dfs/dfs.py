graph = {
    'E': ['C', 'G'],
    'C': ['B', 'D'],
    'G': ['H'],
    'B': [],
    'D': ['H'],
    'H': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

if __name__ == '__main__':
    print('Start visiting everything at E')
    dfs(visited, graph, 'E')
