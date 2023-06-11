friends_items = {
    'Друг 1': ('палатка', 'спальник', 'фонарик', 'еда'),
    'Друг 2': ('рюкзак', 'фонарик', 'карта', 'вода'),
    'Друг 3': ('палатка', 'спальник', 'еда', 'компас'),
    'Друг 4': ('нож', 'кот', 'еда', 'рюкзак')
}

intersec = set.intersection(*[set(items) for items in friends_items.values()])
print("Вещи, взятые всеми тремя друзьями:", intersec)

unique_items = set.union(*[set(items) for items in friends_items.values()]) - intersec
print("Уникальные вещи, есть только у одного друга:", unique_items)

for friend, items in friends_items.items():
    other_friends_items = set.union(*[set(items) for name, items in friends_items.items() if name != friend])
    difference = other_friends_items - set(items)
    if difference:
        print("У всех друзей, кроме", friend, "есть вещи:", difference)

