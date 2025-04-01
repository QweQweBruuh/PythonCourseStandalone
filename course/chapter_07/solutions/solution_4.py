numbers = [12, -7, 5, -3, 8, -2]
new_era = []
for i in numbers:
    if i > 0:
        new_era.append(i)
    if i < 0:
        new_era.append(0)
print("Список после замены:",new_era)