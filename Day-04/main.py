def part_one() -> int:
    numbers_to_call, boards = process_input(input_file)
    for i in range(5, len(numbers_to_call)):
        has_bingo = check_bingo(numbers_to_call[0:i], boards)
        if has_bingo:
            return calculate_score(has_bingo[1], has_bingo[2])


def process_input(file: str):
    with open(file) as f:
        data = [line for line in f.read().split("\n") if line != ""]
        numbers_to_call = [int(i) for i in data[0].split(",")]
        board_data = [list(map(int, d.split())) for d in data[1:]]

        boards = []
        for i in range(0, len(board_data), 5):
            boards.append(board_data[i:i + 5])

        return numbers_to_call, boards


def check_bingo(numbers_called: list, boards: list) -> tuple:
    for board in boards:
        for row in board:
            if set(row).issubset(numbers_called):
                return True, numbers_called, board

        for i in range(len(board[0])):
            column = [row[i] for row in board]
            if set(column).issubset(numbers_called):
                return True, numbers_called, board


def calculate_score(numbers_called: list, winning_board: list) -> int:
    score = numbers_called[-1] * sum([num for row in winning_board for num in row if num not in numbers_called])
    return score


input_file = "./input.txt"
print(f"Part One: {part_one()}")
