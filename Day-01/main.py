def part_one(file: str) -> int:
    with open(file) as f:
        count = 0
        depths = [int(i) for i in f.readlines()]
        for i in range(len(depths) - 1):
            if depths[i + 1] > depths[i]:
                count += 1
        return count


print(part_one("input.txt"))
