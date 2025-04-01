a = int(input())
p = input()
if a>=18 and p == "Y":
    print("Добро пожаловать в клуб!")
elif 0<=a<=17 or p == "N":
    print("Извините, вход запрещен.")
else:
    print("Введите корректные значения.")
    