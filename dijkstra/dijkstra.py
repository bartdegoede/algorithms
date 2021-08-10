from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, source, target):
    # queue will have tuples with (distance_from_source, node, path)
    queue = [(0, source, ())]
    seen = set()
    distances = { source: 0 }

    while queue:
        cost, node, path = heappop(queue)
        if node not in seen:
            seen.add(node)
            path = (node, path)
            if node == target:
                return (cost, path)
            for next_cost, next_node in graph[node]:
                if next_node in seen:
                    continue
                previous = distances.get(next_node, None)
                next = cost + next_cost
                if not previous or next < previous:
                    distances[next_node] = next
                    heappush(queue, (next, next_node, path))
    return float('inf'), None

if __name__ == '__main__':
    edges = [
        ('A', 'B', 7),
        ('A', 'D', 5),
        ('B', 'C', 8),
        ('B', 'D', 9),
        ('B', 'E', 7),
        ('C', 'E', 5),
        ('D', 'E', 15),
        ('D', 'F', 6),
        ('E', 'F', 8),
        ('E', 'G', 9),
        ('F', 'G', 11)
    ]

    graph = defaultdict(list)
    for source, target, distance in edges:
        # list of (distance, target) so we can sort by distance using a heap
        graph[source].append((distance, target))

    print('A -> E:')
    print(dijkstra(graph, 'A', 'E'), '\n')
    print('F -> G:')
    print(dijkstra(graph, 'F', 'G'), '\n')
    print('Non-existing:')
    print(dijkstra(graph, 'X', 'G'), '\n')
