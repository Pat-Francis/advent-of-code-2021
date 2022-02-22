def process_input(file: str):
    with open(file) as f:
        data = f.read().strip()

    return bin(int(data, 16))[2:].zfill(len(data) * 4)


def parse_data(data: str):
    if len(data) == 0:
        return []

    packet_version = int(data[0:3], 2)
    packet_type_id = int(data[3:6], 2)
    last_bit = 6

    if packet_type_id == 4:
        continue_reading = True
        binary_number = ""

        while continue_reading:
            binary_number += data[last_bit + 1: last_bit + 5]
            continue_reading = bool(int(data[last_bit: last_bit + 1]))
            last_bit += 5

        print(f"Literal packet value: {int(binary_number, 2)}")
        return int(binary_number, 2)
    else:
        pass


def part_one(filename: str):
    data = process_input(filename)
    parsed_data = parse_data(data)


input_file = "./test_input.txt"
print(f"Part One: {part_one(input_file)}")
