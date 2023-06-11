def get_unique_duplicates(lst):
    unique_duplicates = []
    count_dict = {}
    
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    for item, count in count_dict.items():
        if count > 1:
            unique_duplicates.append(item)
    
    return unique_duplicates
duplicates = [1, 2, 2, 3, 4, False, 4, 4, 5, 5, 5, 5, 5, 5, 5, "False", 5, 2, 2, 2, 2, 2, 2, "False","False",False,False]
result = get_unique_duplicates(duplicates)
print(result)