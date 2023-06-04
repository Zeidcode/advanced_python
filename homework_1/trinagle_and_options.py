def trinagle_creation(a,b,c):
    if a + b > c and a + c > b and c + b > a :
        print("Введенными данными невозможно построение треугольника")
    else:
        print("Данные корректны для создания треугольника ")

def trinagle_opt(a,b,c):
    if a==b and a==c:
        print("Треугольник равносторонний ")
    elif a==b or a==c or b==c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

# Стороны треугольника
a = int(input("Введите длину стороны a:"))
b = int(input("Введите длину стороны b:"))
c = int(input("Введите длину стороны c:"))


trinagle_creation(a,b,c)
trinagle_opt(a,b,c)