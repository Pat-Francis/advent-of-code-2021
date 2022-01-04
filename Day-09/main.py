def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def is_low_point(array: list[list[int]], x: int, y: int) -> bool:
    indices = []
    adjacency_matrix = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for dx, dy in adjacency_matrix:
        if 0 <= x + dx < len(array) and 0 <= y + dy < len(array[x]):
            indices.append(array[x + dx][y + dy])

    return array[x][y] < min(indices)


def part_one(filename: str) -> int:
    data = process_input(filename)
    risk_level = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            if is_low_point(data, x, y):
                risk_level += 1 + data[x][y]

    return risk_level


def part_two(filename: str):
    data = process_input(filename)

    for x in range(len(data)):
        for y in range(len(data[x])):
            if is_low_point(data, x, y):
                pass


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")