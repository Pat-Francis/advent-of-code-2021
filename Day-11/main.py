adjacency_matrix = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def part_one(filename: str) -> int:
    data = process_input(filename)
    flashes = 0

    for i in range(100):
        to_flash = []
        data = [[num + 1 for num in line] for line in data]
        over_nine = [num for row in data for num in row if num > 9]

        while len(over_nine) > 0:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if data[x][y] > 9:
                        to_flash.append([x, y])
                        for dx, dy in adjacency_matrix:
                            if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]):
                                data[x + dx][y + dy] += 1

            for x, y in to_flash:
                data[x][y] = 0

            over_nine = [num for row in data for num in row if num > 9]
        flashes += len(to_flash)

    return flashes


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")