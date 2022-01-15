from collections import defaultdict
from collections.abc import Callable


def process_input(file: str) -> dict[str, list[str]]:
    data = defaultdict(list)

    with open(file) as f:
        split_data = [line.strip().split("-") for line in f.read().splitlines()]

        for (start, end) in split_data:
            data[start].append(end)
            data[end].append(start)

    return data


def calculate_paths(graph: dict[str, list[str]], start, end: str, visited: Callable, path=[]) -> list[list[str]]:
    path = path + [start]

    if start == end:
        return [path]

    paths = []

    for node in graph[start]:
        if node not in path or visited(path, node):
            new_paths = calculate_paths(graph, node, end, visited, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


def part_one(filename: str):
    graph = process_input(filename)
    return len(calculate_paths(graph, "start", "end", is_upper))


def is_upper(path: list[str], node: str) -> bool:
    return node.isupper()


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
