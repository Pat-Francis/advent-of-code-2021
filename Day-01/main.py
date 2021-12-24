def part_one(file: str) -> int:
    with open(file) as f:
        depths = [int(i) for i in f.readlines()]
        return sliding_window(depths, 1)


def part_two(file: str) -> int:
    with open(file) as f:
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
print(f"Part One: {part_two(input_file)}")
