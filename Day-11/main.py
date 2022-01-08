adjacency_matrix = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def process_input(file: str) -> list[list[int]]:
    with open(file) as f:
        return [list(map(int, line)) for line in f.read().split()]


def part_one(filename: str):
    data = process_input(input_file)
    for line in data:
        print(line)


input_file = "./test_input.txt"
print(f"Part One: {part_one(input_file)}")