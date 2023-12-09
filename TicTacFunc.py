# Проверка корректности имени игрока
def check_name(name: str):
    while not name.isalpha():
        name = input("Некорректное имя. Введите имя игрока: ")
    print(f"Спасибо, игрок - {name}")
    return name


# Первое отображение поля
def start_field(field):
    for i in range(3):
        if i == 0:
            print("  0 ", " 1 ", " 2 ", sep="")
        for j in range(3):
            print(i if j == 0 else '', end="")
            print(field[i][j], end="")
        print()


# Проверка победителя
def check_winner(field):
    # Проверка по горизонтали и вертикали
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != " - ":
            return field[i][0]
        if field[0][i] == field[1][i] == field[2][i] != " - ":
            return field[0][i]

    # Проверка по диагоналям
    if field[0][0] == field[1][1] == field[2][2] != " - ":
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != " - ":
        return field[0][2]

    return None  # Если нет победителя


# Запуск начала игры
def start_window():
    print("Привет! Давай начнём игру в крестики-нолики\n")

    # Заполнение стартового поля
    start_field([[" - " for j in range(3)] for i in range(3)])

    print("\nСмотри, это стартовое поле, идея заполнения довольно проста, для начала давай определимся, "
          "кто будет играть.\n")

    # Считывание имён игроков
    print("P.S. Имя должно состоять лишь из буквенных символов, а начинать всегда будет первый игрок с крестика")
    first = check_name(input("Введите имя первого игрока: "))
    second = check_name(input("Введите имя второго игрока: "))
    return first, second


# Ввод хода
def get_move(player, field):
    while True:
        try:
            input_str = input(f"{player}, введи номер строки и столбца через пробел (для выхода введите 'exit'): ")
            if input_str.lower() == 'exit':
                print("Игра завершена.")
                exit()

            coordinates = list(map(int, input_str.split()))
            x, y = coordinates
            if len(coordinates) != 2 or not (0 <= x <= 2 and 0 <= y <= 2) or field[x][y] != " - ":
                raise ValueError
            return x, y
        except ValueError:
            print(f"Ошибка: Некорректные координаты. Попробуйте ещё раз.")


# Заполнение поля и вывод победителя
def main_game(first, second):
    print("\nТеперь начнём игру. Верхняя строка, состоящая из цифр, и левая колонка, также состоящая из цифр, "
          "позволяет определить ту позицию, куда ты хочешь поставить отметку. Для выхода введите 'exit'.\n")

    field = [[" - " for _ in range(3)] for _ in range(3)]
    winner = None

    for i in range(9):
        player = first if i % 2 == 0 else second
        x, y = get_move(player, field)
        field[x][y] = " X " if i % 2 == 0 else " O "

        print()
        start_field(field)
        print()

        winner = check_winner(field)
        if winner:
            print(f"Поздравляем! Игрок {second} победил!" if winner == "X" else f"Поздравляем! Игрок {first} победил!")
            exit()

    if not winner:
        print("Ничья! Игра завершена.")


# Вызовы функций
a, b = start_window()
main_game(a, b)
