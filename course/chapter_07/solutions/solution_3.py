numbers = [3, 17, 6, 12, 9, 21, 5]
mx = numbers[0]
mn = numbers[0]
for i in numbers:
    if i > mx:
        mx = i
print(f"Максимальный элемент: {mx}")
    