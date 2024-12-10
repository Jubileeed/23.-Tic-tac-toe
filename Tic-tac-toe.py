# Инициализация доски
board = list(range(1, 10))

# Вывод доски на экран
print("-" * 13)
for i in range(3):
    print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("-" * 13)

counter = 1  # Счетчик ходов
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # Комбинации выигрышных позиций
win = False  # Отметка, указывающая на окончание игры (победа или ничья)

# Цикл игры
while not win:
    # Определение текущего игрока
    player = "X" if counter % 2 != 0 else "O"

    # Получение ввода от игрока
    player_input = int(input(f"Куда поставим {player}? "))

    # Проверка корректности ввода и занятости клетки
    if board[player_input - 1] not in ["X", "O"]:
        board[player_input - 1] = player
        counter += 1
    else:
        print("Эта клетка уже занята!")
        continue

    # Вывод обновленной доски на экран
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

    # Проверка наличия выигрышной комбинации
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            print(board[each[0]], "выиграл!")
            win = True
            break
    # Проверка на ничью
    if counter == 10 and not win:
        print("Ничья!")
        break

# Ожидание ввода для завершения программы
input("Нажмите Enter для выхода!")