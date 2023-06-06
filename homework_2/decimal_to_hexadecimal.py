def decimal_to_hexadecimal(number):
    return hex(number)


decimal_number: int = int(input("Введите целое число: "))


hexadecimal_string = decimal_to_hexadecimal(decimal_number)

print("Шестнадцатеричное представление числа:", hexadecimal_string)


hex_check = hex(decimal_number)
print("Проверка с помощью функции hex():", hex_check)