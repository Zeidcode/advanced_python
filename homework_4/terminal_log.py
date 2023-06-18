import math

balance = 0
transactions = []

def deposit(amount):
    global balance
    global transactions
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    balance += amount
    transactions.append(("Пополнение", amount))
    if len(transactions) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transactions.append(("Проценты", interest))
    print(f"Баланс: {balance}")

def withdraw(amount):
    global balance
    global transactions
    if amount % 50 != 0:
        print("Сумма должна быть кратна 50")
        return
    if amount > balance:
        print("Недостаточно средств на счете")
        return
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        transactions.append(("Налог на богатство", tax))
    fee = max(amount * 0.015, 30)
    fee = min(fee, 600)
    balance -= amount + fee
    transactions.append(("Снятие", amount))
    if len(transactions) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transactions.append(("Проценты", interest))
    print(f"Баланс: {balance}")

def print_balance():
    global balance
    print(f"Баланс: {balance}")

def print_transactions():
    global transactions
    for transaction in transactions:
        print(f"{transaction[0]}: {transaction[1]}")

while True:
    print("Выберите действие:\n1-пополнить\n2-снять\n3-вывести список транзакций\n4-выйти")
    action = input().lower()
    if action == "1":
        print("Введите сумму для пополнения")
        amount = int(input())
        deposit(amount)
    elif action == "2":
        print("Введите сумму для снятия")
        amount = int(input())
        withdraw(amount)
    elif action == "3":
        print_transactions()
    elif action == "4":
        break
    else:
        print("Неверная команда")

    print()