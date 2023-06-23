names = ['Алиса', 'Тимур', 'Евгений']
rates = []

for name in names:
    rate = int(input(f'Введите ставку для {name}: '))
    rates.append(rate)

bonuses = ['10%', '15%', '25%']

result = {name: rate * float(bonus[:-1])/100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result)