password = "mypassword"
count = 0
while count != 3:
    n = str(input())
    count += 1
    if n != password and count < 3:
        print("Неверный пароль, попробуйте снова.")
    if n != password and count == 3:
        print("Доступ запрещен")  
    if n == password:
        print("Доступ разрешён.")
        break