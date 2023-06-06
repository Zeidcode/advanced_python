TAX_THRESHOLD = 5000000
WITHDRAWAL_FEE_PERCENTAGE = 1.5
WITHDRAWAL_FEE_MIN = 30
WITHDRAWAL_FEE_MAX = 600
INTEREST_INTERVAL = 3
INTEREST_RATE = 3.0 / 100

def calculate_withdrawal_fee(amount):
    fee = amount * WITHDRAWAL_FEE_PERCENTAGE / 100
    fee = max(fee, WITHDRAWAL_FEE_MIN)
    fee = min(fee, WITHDRAWAL_FEE_MAX)
    return fee

def calculate_interest(balance):
    interest = balance * INTEREST_RATE
    return interest

def calculate_tax(balance):
    tax = balance * 0.1
    return tax

def main():
    balance = 0
    operation_count = 0

    while True:
        print("Текущий баланс:", balance)
        print("Допустимые действия: пополнить, снять, выйти")
        action = input("Введите действие: ")

        if action == "пополнить":
            deposit = int(input("Введите сумму пополнения (кратную 50): "))
            if deposit % 50 != 0:
                print("Сумма пополнения должна быть кратной 50.")
                continue
            balance += deposit

        elif action == "снять":
            withdrawal = int(input("Введите сумму снятия (кратную 50): "))
            if withdrawal % 50 != 0:
                print("Сумма снятия должна быть кратной 50.")
                continue
            if withdrawal > balance:
                print("Недостаточно средств на счете.")
                continue
            fee = calculate_withdrawal_fee(withdrawal)
            balance -= withdrawal + fee

        elif action == "выйти":
            break

        else:
            print("Недопустимое действие.")
            continue

        if balance >= TAX_THRESHOLD:
            tax = calculate_tax(balance)
            balance -= tax

        operation_count += 1
        if operation_count % INTEREST_INTERVAL == 0:
            interest = calculate_interest(balance)
            balance += interest

    print("Итоговый баланс:", balance)

# Запуск основной программы
main()
