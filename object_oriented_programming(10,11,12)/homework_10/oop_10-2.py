import random
from itertools import combinations


class Chessboard:
    def __init__(self):
        self.queens = []
        self.successful_arrangements = []

    def generate_arrangement(self):
        self.queens = [(i, random.randint(1, 8)) for i in range(1, 9)]

    def is_valid(self):
        for queen1, queen2 in combinations(self.queens, 2):

            if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
                return False

            if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
                return False

        return True

    def solve(self):
        while len(self.successful_arrangements) < 4:
            self.generate_arrangement()
            if self.is_valid():
                self.successful_arrangements.append(self.queens)

    def print_successful_arrangements(self):
        for idx, arrangement in enumerate(self.successful_arrangements):
            print(f"Успешная расстановка {idx + 1}: {arrangement}")


chessboard = Chessboard()
chessboard.solve()
chessboard.print_successful_arrangements()
