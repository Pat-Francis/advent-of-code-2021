from collections import defaultdict
from heapq import heappop, heappush


def process_input(file: str):
    with open(file) as f:
        data = [list(map(int, line)) for line in f.read().split()]

    return data


def generate_edges(data):
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
    queue = [(0, start)]

    while queue:
        path_len, vertex = heappop(queue)

        if vertex == end:
            return path_len

        if unvisited[vertex] == float("inf"):
            unvisited[vertex] = path_len
            for neighbour, cost in edges[vertex].items():
                if unvisited[neighbour] == float("inf"):
                    heappush(queue, (path_len + cost, neighbour))


def part_one(filename: str):
    data = process_input(filename)
    vertices, edges = generate_edges(data)
    start = min(vertices)
    end = max(vertices)

    return dijkstra(vertices, edges, start, end)


def part_two(filename: str):
    data = process_input(filename)

    # extend columns
    column_ext = data
    for _ in range(4):
        column_ext = [[i % 9 + 1 for i in row] for row in column_ext]
        for i, _ in enumerate(data):
            data[i] = data[i] + column_ext[i]

    # extend rows
    extended_rows = []
    row_ext = data
    for _ in range(4):
        row_ext = [[i % 9 + 1 for i in row] for row in row_ext]
        extended_rows = extended_rows + row_ext

    data = data + extended_rows
    vertices, edges = generate_edges(data)
    start = min(vertices)
    end = max(vertices)

    return dijkstra(vertices, edges, start, end)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part One: {part_two(input_file)}")
