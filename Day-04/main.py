def process_input(file: str) -> tuple:
    with open(file) as f:
        data = [line for line in f.read().split("\n") if line != ""]
        numbers_to_call = [int(i) for i in data[0].split(",")]
        board_data = [list(map(int, d.split())) for d in data[1:]]

        boards = []
        for i in range(0, len(board_data), 5):
            boards.append(board_data[i:i + 5])

        return numbers_to_call, boards


def check_bingo(numbers_called: list, board: list) -> bool:
    for row in board:
        if set(row).issubset(numbers_called):
            return True

    for i in range(len(board[0])):
        column = [row[i] for row in board]
        if set(column).issubset(numbers_called):
            return True


def calculate_score(numbers_called: list, winning_board: list) -> int:
    score = numbers_called[-1] * sum([num for row in winning_board for num in row if num not in numbers_called])
    return score


def part_one() -> int:
    numbers_to_call, boards = process_input(input_file)
    for i in range(len(numbers_to_call)):
        for board in boards:
            if check_bingo(numbers_to_call[0:i], board):
                return calculate_score(numbers_to_call[0:i], board)


def part_two() -> int:
    numbers_to_call, boards = process_input(input_file)
    for i in range(len(numbers_to_call)):
        non_winning_boards = []
        for board in boards:
            if not check_bingo(numbers_to_call[0:i], board):
                non_winning_boards.append(board)
            else:
                if len(boards) == 1:
                    return calculate_score(numbers_to_call[0:i], board)

        boards = non_winning_boards


input_file = "./input.txt"
print(f"Part One: {part_one()}")
print(f"Part One: {part_two()}")
