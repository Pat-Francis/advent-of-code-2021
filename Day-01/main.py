def part_one(filename: str) -> int:
    with open(filename) as f:
        depths = [int(i) for i in f.readlines()]
    return sliding_window(depths, 1)


def part_two(filename: str) -> int:
    with open(filename) as f:
        depths = [int(i) for i in f.readlines()]
    return sliding_window(depths, 3)


def sliding_window(numbers: list[int], window: int) -> int:
    count = 0
    for i in range(len(numbers) - window):
        if numbers[i + window] > numbers[i]:
            count += 1
    return count


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
