from collections import defaultdict


def process_input(file: str):
    with open(file) as f:
        data = [list(map(int, line)) for line in f.read().split()]
        adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vertices = []

        for i in range(len(data)):
            for j in range(len(data[0])):
                vertices.append((i, j))

        edges = defaultdict(list)
        for x, y in vertices:
            for dx, dy in adjacent:
                if 0 <= x + dx <= len(data) and 0 <= y + dy <= len(data[0]) and (x + dx, y + dy) != (0, 0):
                    edges[(x, y)].append((x + dx, y + dy))
        print(edges)


def dijkstra():
    pass


def part_one(filename: str):
    return process_input(filename)


input_file = "./test_input.txt"
print(f"Part One: {part_one(input_file)}")