class TicTac:
    # Задаём атрибуты для экземпляра
    def __init__(self):
        self.field = [[" - " for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.players = []

    # Запуск начала игры
    def start_window(self):
        print("Привет! Давай начнём игру в крестики-нолики\n")
        self.start_field()

        print("\nСмотри, это стартовое поле, идея заполнения довольно проста, для начала давай определимся, "
              "кто будет играть.\n")
        self.get_player_names()

        print("\nТеперь начнём игру. Верхняя строка, состоящая из цифр, и левая колонка, также состоящая из цифр, "
              "позволяет определить ту позицию, куда ты хочешь поставить отметку. Для выхода введите 'exit'.\n")

        winner = None
        for i in range(9):
            self.current_player = self.players[i % 2]
            x, y = self.get_move()
            self.field[x][y] = " X " if i % 2 == 0 else " O "

            print()
            self.start_field()
            print()

            winner = self.check_winner()
            if winner:
                print(f"Поздравляем! Игрок {self.players[1]} победил!" if winner == "X"
                      else f"Поздравляем! Игрок {self.players[0]} победил!")
                return

        if not winner:
            print("Ничья! Игра завершена.")

    # Первое отображение поля
    def start_field(self):
        for i in range(3):
            if i == 0:
                print("  0 ", " 1 ", " 2 ", sep="")
            for j in range(3):
                print(i if j == 0 else '', end="")
                print(self.field[i][j], end="")
            print()

    # Считывание имён
    def get_player_names(self):
        print("P.S. Имя должно состоять лишь из буквенных символов, а начинать всегда будет первый игрок с крестика")
        for _ in range(2):
            name = self.check_name(input("Введите имя игрока: "))
            self.players.append(name)

    # Проверка корректности имени игрока
    @staticmethod
    def check_name(name):
        while not name.isalpha():
            name = input("Некорректное имя. Введите имя игрока: ")
        print(f"Спасибо, игрок - {name}")
        return name

    # Ввод хода
    def get_move(self):
        while True:
            try:
                input_str = input(
                    f"{self.current_player}, введи номер строки и столбца через пробел (для выхода введите 'exit'): ")
                if input_str.lower() == 'exit':
                    print("Игра завершена.")
                    exit()

                coordinates = list(map(int, input_str.split()))
                x, y = coordinates
                if len(coordinates) != 2 or not (0 <= x <= 2 and 0 <= y <= 2) or self.field[x][y] != " - ":
                    raise ValueError
                return x, y
            except ValueError:
                print(f"Ошибка: Некорректные координаты. Попробуйте ещё раз.")

    # Определение победителя
    def check_winner(self):
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != " - ":
                return self.field[i][0]
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != " - ":
                return self.field[0][i]

        if self.field[0][0] == self.field[1][1] == self.field[2][2] != " - ":
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != " - ":
            return self.field[0][2]

        return None


# Экземпляр игры
game = TicTac()
game.start_window()
