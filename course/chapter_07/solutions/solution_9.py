numbers = []
n = input()
while n != "":
    numbers.append(int(n))
    n = input()
print("Минимальная оценка:",min(numbers))
print("Максимальная оценка:",max(numbers))
numbers.sort()
print("Отсортированные оценки:",numbers)

    