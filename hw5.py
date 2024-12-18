import random


def play_game(min_number, max_number, attempts, initial_balance):
    """
    Основная логика игры "Угадай число".

    Args:
        min_number (int): Минимальное число диапазона.
        max_number (int): Максимальное число диапазона.
        attempts (int): Количество попыток.
        initial_balance (int): Начальный баланс игрока.
    """
    print("\nДобро пожаловать в игру 'Угадай число'!")
    print(f"Ваш начальный баланс: {initial_balance} монет.")
    print(f"Угадайте число от {min_number} до {max_number}. У вас {attempts} попытки(ок).\n")

    balance = initial_balance
    secret_number = random.randint(min_number, max_number)

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt} из {attempts}. Ваш текущий баланс: {balance} монет.")
        try:
            # Получение ставки
            bet = int(input("Введите ставку: "))
            if bet > balance or bet <= 0:
                print("Ставка должна быть положительной и не превышать ваш баланс. Попробуйте снова.")
                continue

            # Угадывание числа
            guess = int(input(f"Введите число ({min_number}-{max_number}): "))
            if guess < min_number or guess > max_number:
                print("Число вне диапазона. Попробуйте снова.")
                continue

            # Проверка результата
            if guess == secret_number:
                print("Поздравляем! Вы угадали число!")
                balance += bet
                print(f"Ваш баланс увеличился до {balance} монет.\n")
                break
            else:
                print("Неверно! Вы теряете ставку.")
                balance -= bet
                if balance <= 0:
                    print("У вас закончились деньги. Игра окончена.")
                    break
        except ValueError:
            print("Ошибка ввода! Введите корректное число.")

    else:
        print(f"\nВы исчерпали все попытки. Загаданное число было: {secret_number}.")

    print(f"Ваш итоговый баланс: {balance} монет.")
    return balance


from decouple import Config, RepositoryIni
from logic import play_game


def main():
    """
    Главный модуль для запуска игры. Считывает настройки из файла settings.ini
    и передает их в модуль с логикой игры.
    """
    config = Config(RepositoryIni('settings.ini'))

    # Получение настроек из файла
    min_number = config.getint('game.min_number')
    max_number = config.getint('game.max_number')
    attempts = config.getint('game.attempts')
    initial_balance = config.getint('game.initial_balance')

    # Запуск игры
    play_game(min_number, max_number, attempts, initial_balance)


if __name__ == "__main__":
    main()

[game]
min_number = 1
max_number = 10
attempts = 3
initial_balance = 100

# source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows
#
# python main.py
