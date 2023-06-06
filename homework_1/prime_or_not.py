def prime_or_not(a):
    if a < 0 or a > 100000:
        print(f"Введенное число {a} вне допустимого диапазона.\nДопустимый диапазон от 0 строго до 100000.")
    else:
        is_prime = True
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                is_prime = False
                break

        if is_prime and a > 1:
            print(f"Число {a} является простым.")
        else:
            print(f"Число {a} не является простым.")


a = int(input("Введите число в диапазоне от 0 строго до 100000: "))
prime_or_not(a)
