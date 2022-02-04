from collections import defaultdict


def process_input(file: str):
    with open(file) as f:
        data = [list(map(int, line)) for line in f.read().split()]
        adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vertices = []

        for i, _ in enumerate(data):
            for j, _ in enumerate(data[0]):
                vertices.append((i, j))

        edges = defaultdict(dict)
        for x, y in vertices:
            for dx, dy in adjacent:
                if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
                    edges[x, y].update({(x + dx, y + dy): data[x + dx][y + dy]})

    return vertices, edges


def dijkstra(vertices, edges, start, end) -> int:
    unvisited = {vertex: float("inf") for vertex in vertices}
    unvisited[start] = 0
    visited = {}
    parent = {}

    while unvisited:
        min_node = min(unvisited, key=unvisited.get)

        for neighbour, cost in edges[min_node].items():
            if neighbour not in visited:
                new_distance = unvisited[min_node] + cost
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parent[neighbour] = min_node

        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)

    return visited[end]


def part_one(filename: str):
    vertices, edges = process_input(filename)
    start = min(vertices)
    end = max(vertices)

    return dijkstra(vertices, edges, start, end)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")