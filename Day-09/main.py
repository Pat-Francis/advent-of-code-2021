def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def part_one(filename: str) -> int:
    data = process_input(filename)
    adjacency_matrix = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    risk_level = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            indices = []

            for dx, dy in adjacency_matrix:
                if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]):
                    indices.append((x + dx, y + dy))

            adjacent_values = [data[i][j] for (i, j) in indices]
            current_value = data[x][y]

            if all([current_value < i for i in adjacent_values]):
                risk_level += 1 + current_value

    return risk_level


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
