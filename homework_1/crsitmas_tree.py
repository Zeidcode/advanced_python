def draw_christmas_tree(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    print(' ' * (rows - 1) + '|')
    print(' ' * (rows - 1) + '|')


num_rows = int(input("Введите число : "))

draw_christmas_tree(num_rows)