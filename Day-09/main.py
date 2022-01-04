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


def part_two(filename: str) -> list[tuple]:
    data = process_input(filename)
    adjacency_matrix = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    lowest_points = []

    for x in range(len(data)):
        for y in range(len(data[x])):
            indices = []

            for dx, dy in adjacency_matrix:
                if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]):
                    indices.append((x + dx, y + dy))

            adjacent_values = [data[i][j] for (i, j) in indices]
            current_value = data[x][y]

            if all([current_value < i for i in adjacent_values]):
                lowest_points.append((x, y))

    basin_sizes = []

    for point in lowest_points:
        basin = []
        indices_to_check = [point]
        print(indices_to_check)
        for x, y in indices_to_check:
            print(f"Index: {x, y}")
            for dx, dy in adjacency_matrix:
                if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]) and data[x + dx][y + dy] < 9:
                    print(f"check 2: {x + dx} - {y + dy}")



input_file = "./test_input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
