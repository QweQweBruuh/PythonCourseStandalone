numbers = [4, 7, 2, 9, 8, 5, 6, 3, 0, 1]
chet = []
for i in numbers:
    if i % 2 == 0:
        chet.append(numbers.index(i))
print(*chet,sep = ", ")