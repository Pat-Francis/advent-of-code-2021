def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def is_low_point(array: list[list[int]], x: int, y: int) -> bool:
    adjacent = []
    adjacency_matrix = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for dx, dy in adjacency_matrix:
        if 0 <= x + dx < len(array) and 0 <= y + dy < len(array[x]):
            adjacent.append(array[x + dx][y + dy])

    return array[x][y] < min(adjacent)


def calculate_basin(visited: set, array: list[list[int]], x, y):
    adjacent = []
    adjacency_matrix = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    if (x, y) not in visited:
        visited.add((x, y))

    for dx, dy in adjacency_matrix:
        if 0 <= x + dx < len(array) and 0 <= y + dy < len(array[x]) and array[x + dx][y + dy] != 9:
            # print(x + dx, y + dy)
            adjacent.append((x + dx, y + dy))

    for (x, y) in adjacent:
        if (x, y) not in visited:
            calculate_basin(visited, array, x, y)
    else:
        return len(visited)


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
    lowest_points = []
    basin_sizes = []

    for x in range(len(data)):
        for y in range(len(data[x])):
            if is_low_point(data, x, y):
                lowest_points.append([x, y])

    for point in lowest_points:
        basin = set()

        basin_size = calculate_basin(basin, data, point[0], point[1])
        basin_sizes.append(basin_size)

    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")