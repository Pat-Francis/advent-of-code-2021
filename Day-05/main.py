from collections import defaultdict


def process_input(file: str) -> list[list[tuple]]:
    with open(file) as f:
        data = list(map(lambda line: line.strip().split(" -> "), f.readlines()))
        lines = [[tuple(map(int, line[0].split(","))), tuple(map(int, line[1].split(",")))] for line in data]

        return lines


def process_lines(co_ords: dict, start: tuple, end: tuple) -> dict[tuple, int]:
    x_steps = 0 if start[0] == end[0] else int(end[0] - start[0]) // int(abs(start[0] - end[0]))
    y_steps = 0 if start[1] == end[1] else int(end[1] - start[1]) // int(abs(start[1] - end[1]))

    distance = max(abs(start[0] - end[0]), abs(start[1] - end[1]))

    for i in range(distance + 1):
        x = start[0] + i * x_steps
        y = start[1] + i * y_steps
        co_ords[(x, y)] += 1

    return co_ords


def count_overlaps(points: dict) -> int:
    return len({k for k, v in points.items() if v >= 2})


def part_one(filename: str) -> int:
    lines = process_input(filename)
    lines_dict = defaultdict(int)
    for start, end in lines:
        if start[0] == end[0] or start[1] == end[1]:
            lines_dict = process_lines(lines_dict, start, end)

    return count_overlaps(lines_dict)


def part_two(filename: str) -> int:
    lines = process_input(filename)
    lines_dict = defaultdict(int)
    for start, end in lines:
        lines_dict = process_lines(lines_dict, start, end)

    return count_overlaps(lines_dict)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
