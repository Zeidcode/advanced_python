def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: x[1])
    
    backpack = {}
    total_weight = 0
    
    for item, weight in sorted_items:
        if total_weight + weight <= max_weight:
            backpack[item] = weight
            total_weight += weight
    
    return backpack



items = {
    'Книга': 1,
    'Вода': 3,
    'Еда': 2,
    'Куртка': 2,
    'Палатка': 5,
    'Фонарик': 1
}

max_weight = 10

backpack = fill_backpack(items, max_weight)

print("Вещи в рюкзаке:")
for item, weight in backpack.items():
    print(f"{item}: {weight} кг")
