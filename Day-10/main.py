from statistics import median

part_one_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

part_two_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def process_input(file: str) -> list[str]:
    with open(file) as f:
        return [line for line in f.read().split()]


def part_one(filename: str) -> int:
    data = process_input(filename)
    score = 0

    for line in data:
        open_chars = []
        for char in line:
            if char in open_to_close:
                open_chars.append(char)
            elif open_to_close.get(open_chars[-1]) == char:
                open_chars.pop()
            else:
                score += part_one_points.get(char)
                break

    return score


def part_two(filename: str) -> int:
    data = process_input(filename)
    scores = []
    for line in data:
        open_chars = []
        corrupt = False
        for char in line:
            if char in open_to_close:
                open_chars.append(char)
            elif open_to_close.get(open_chars[-1]) == char:
                open_chars.pop()
            else:
                corrupt = True
                break
        if not corrupt:
            score = 0
            for char in open_chars[::-1]:
                score = score * 5 + part_two_points.get(open_to_close.get(char))
            scores.append(score)

    return median(scores)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
