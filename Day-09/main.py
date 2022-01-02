def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def adjacent_indices(array: list[list], x_coord: int, y_coord: int) -> list[tuple]:
    adjacent = []
    adjacency_matrix = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

    for dx, dy in adjacency_matrix:
        if 0 <= x_coord + dx < len(array) and 0 <= y_coord + dy < len(array[0]):
            adjacent.append((x_coord + dx, y_coord + dy))

    return adjacent


def part_one(filename: str) -> int:
    data = process_input(filename)
    risk_level = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            indices = adjacent_indices(data, x, y)

            # Remove diagonal indices
            indices = [(i, j) for (i, j) in indices if i == x or j == y]

            adjacent_values = [data[i][j] for (i, j) in indices]
            current_value = data[x][y]

            if all([current_value < i for i in adjacent_values]):
                risk_level += 1 + current_value
    return risk_level


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
