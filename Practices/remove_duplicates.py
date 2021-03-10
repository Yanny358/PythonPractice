numbers = [2, 5, 7, 2, 3, 5, 3, 7, 8, 4, 6, 4, 7, 6, 5]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)