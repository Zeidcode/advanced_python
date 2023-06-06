def calculate_fraction_operations(fraction1, fraction2):
    # Разделение числителя и знаменателя для первой дроби
    num1, den1 = map(int, fraction1.split('/'))

    # Разделение числителя и знаменателя для второй дроби
    num2, den2 = map(int, fraction2.split('/'))

    # Вычисление суммы дробей
    sum_num = num1 * den2 + num2 * den1
    sum_den = den1 * den2

    # Вычисление произведения дробей
    prod_num = num1 * num2
    prod_den = den1 * den2

    # Приведение суммы и произведения к несократимому виду
    gcd_sum = calculate_gcd(sum_num, sum_den)
    sum_num //= gcd_sum
    sum_den //= gcd_sum

    gcd_prod = calculate_gcd(prod_num, prod_den)
    prod_num //= gcd_prod
    prod_den //= gcd_prod

    # Возвращение результатов в виде строк
    sum_fraction = str(sum_num) + '/' + str(sum_den)
    prod_fraction = str(prod_num) + '/' + str(prod_den)

    return sum_fraction, prod_fraction

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Получение дробей от пользователя
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Вычисление операций с дробями
sum_fraction, prod_fraction = calculate_fraction_operations(fraction1, fraction2)

# Вывод результатов
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", prod_fraction)