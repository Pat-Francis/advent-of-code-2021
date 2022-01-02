from collections import Counter

nums_to_signals = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

signals_to_nums = {''.join(sorted(v)): k for k, v in nums_to_signals.items()}


def process_input(file: str) -> list[list[list]]:
    with open(file) as f:
        data = list(map(lambda line: line.strip().split(" | "), f.readlines()))
        lines = [[list(map(str, line[0].split())), list(map(str, line[1].split()))] for line in data]
        return lines


def decode_signal(signals: list) -> dict:
    decoded = {}

    seven = [x for x in signals if len(x) == len(nums_to_signals[7])][0]
    one = [x for x in signals if len(x) == len(nums_to_signals[1])][0]
    char_a = next(c for c in seven if c not in one)
    decoded[char_a] = "a"

    combined_signals = ''.join(s for s in signals)
    char_counts = Counter(combined_signals)

    for char, count in char_counts.items():
        if count == 4:
            decoded[char] = "e"
        elif count == 6:
            decoded[char] = "b"
        elif count == 9:
            decoded[char] = "f"
        elif count == 7:
            four = [x for x in signals if len(x) == len(nums_to_signals[4])][0]
            if char in four:
                decoded[char] = "d"
            else:
                decoded[char] = "g"
        elif count == 8 and char != char_a:
            decoded[char] = "c"

    return decoded


def part_one(filename: str) -> int:
    lines = process_input(filename)
    unique_nums = [1, 4, 7, 8]
    unique_segments = [len(v) for k, v in nums_to_signals.items() if k in unique_nums]
    count = 0
    for _, outputs in lines:
        for num in outputs:
            if len(num) in unique_segments:
                count += 1
    return count


def part_two(filename: str):
    lines = process_input(filename)
    total = 0
    for signals, outputs in lines:
        cipher = decode_signal(signals)
        decoded_outputs = []

        for output in outputs:
            converted_output = ""
            for char in output:
                converted_output += cipher.get(char)
            decoded_outputs.append(''.join(sorted(converted_output)))

        total += int(''.join(map(str, [signals_to_nums[x] for x in decoded_outputs])))

    return total


input_file = "./input.txt"
print(f"Part One: {part_one(input_file)}")
print(f"Part Two: {part_two(input_file)}")
