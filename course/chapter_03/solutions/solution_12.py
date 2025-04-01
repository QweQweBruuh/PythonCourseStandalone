num = 30
count = 0
while count != 5:
    n = int(input())
    count += 1
    if n > num:
        print("Загаданное число меньше.")
    if n < num:
        print("Загаданное число больше.")
    if count == 5:
        print("Попытки закончились")
    if n == num:
        print("Поздравляем! Вы угадали число.")
        break
        
    