def draw_christmas_tree(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    print(' ' * (rows - 1) + '|')  # Trunk of the tree
    print(' ' * (rows - 1) + '|')  # Trunk of the tree

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows for the Christmas tree: "))

# Draw the Christmas tree
draw_christmas_tree(num_rows)