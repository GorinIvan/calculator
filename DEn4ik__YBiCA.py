import os
from datetime import datetime


def save_statistics(board_size, winner, moves_count):
    # Создаем директорию если ее нет
    if not os.path.exists('game_stats'):
        os.makedirs('game_stats')

    # Создаем файл для статистики
    stats_file = 'game_stats/statistics.txt'

    # Записываем статистику
    with open(stats_file, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = "Ничья" if winner == "Ничья" else f"Победитель: {winner}"
        f.write(f"[{timestamp}] Размер поля: {board_size}x{board_size}, {result}, Ходов: {moves_count}\n")


def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def print_board(board):
    size = len(board)
    for i in range(size):
        print(' | '.join(board[i]))
        if i < size - 1:
            print('-' * (size * 4 - 1))


def check_winner(board):
    size = len(board)

    # Проверка строк
    for row in board:
        if row[0] != ' ' and all(cell == row[0] for cell in row):
            return row[0]

    # Проверка столбцов
    for col in range(size):
        if board[0][col] != ' ' and all(board[row][col] == board[0][col] for row in range(size)):
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]

    if board[0][size - 1] != ' ' and all(board[i][size - 1 - i] == board[0][size - 1] for i in range(size)):
        return board[0][size - 1]

    return None


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def main():
    # Получаем размер поля от пользователя
    while True:
        try:
            size = int(input("Введите размер игрового поля: "))
            if size < 3:
                print("Размер поля должен быть не менее 3")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число")

    board = create_board(size)
    current_player = 'X'
    moves_count = 0

    print(f"\nИгра начинается! Размер поля: {size}x{size}")
    print("Игроки будут ходить по очереди, начиная с X")

    while True:
        print_board(board)

        # Получаем ход от игрока
        while True:
            try:
                move = input(f"Игрок {current_player}, введите строку и столбец (например: 1 2): ")
                row, col = map(int, move.split())

                if row < 1 or row > size or col < 1 or col > size:
                    print(f"Координаты должны быть от 1 до {size}")
                    continue

                if make_move(board, row - 1, col - 1, current_player):
                    moves_count += 1
                    break
                else:
                    print("Эта клетка уже занята!")
            except (ValueError, IndexError):
                print("Пожалуйста, введите два числа через пробел")

        # Проверяем победителя
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} победил!")
            save_statistics(size, winner, moves_count)
            break

        # Проверяем ничью
        if is_board_full(board):
            print_board(board)
            print("Ничья!")
            save_statistics(size, "Ничья", moves_count)
            break

        # Меняем игрока
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()