from collections import Counter, defaultdict


def process_input(file: str) -> list[int]:
    with open(file) as f:
        return list(map(int, f.read().split(",")))


def update_lantern_fish(lantern_fish: list, days: int) -> int:

    all_fish = Counter(lantern_fish)
    for _ in range(days):
        new_fish = defaultdict(int)
        for fish in all_fish:
            if fish == 0:
                new_fish[6] += all_fish[0]
                new_fish[8] += all_fish[0]
            else:
                new_fish[fish - 1] += all_fish[fish]
        all_fish = new_fish

    return sum(all_fish.values())


def part_one(filename: str) -> int:
    return update_lantern_fish(process_input(filename), 80)


def part_two(filename: str) -> int:
    return update_lantern_fish(process_input(filename), 256)


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
