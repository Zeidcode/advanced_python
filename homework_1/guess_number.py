from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

def guess_number():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 10

    print("Угадайте число от", LOWER_LIMIT, "до", UPPER_LIMIT)

    while attempts > 0:
        guess = int(input("Попытка {}: Введите ваше предположение: ".format(11 - attempts)))

        if guess < num:
            print("Загаданное число больше вашего предположения.")
        elif guess > num:
            print("Загаданное число меньше вашего предположения.")
        else:
            print("Поздравляю! Вы угадали число.")
            return

        attempts -= 1

    print("Вы исчерпали все попытки. Загаданное число было", num)

guess_number()
