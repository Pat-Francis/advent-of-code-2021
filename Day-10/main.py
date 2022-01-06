points_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def process_input(file: str) -> list[str]:
    with open(file) as f:
        return [line for line in f.read().split()]


def part_one(filename: str) -> int:
    data = process_input(filename)
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    score = 0

    for line in data:
        open_chars = []
        for char in line:
            if char in openers:
                open_chars.append(char)
            elif open_chars[-1] == openers[closers.index(char)]:
                open_chars = open_chars[:-1]
            else:
                score += points_dict.get(char)
                break
    return score


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
