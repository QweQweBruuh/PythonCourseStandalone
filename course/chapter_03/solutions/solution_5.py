password = "12345678"
i = input()
if i != password:
        print("Неверный пароль, попробуйте снова.")
if i == password:
    print("Доступ разрешён.")
while i != password:
    i = input()
    if i != password:
        print("Неверный пароль, попробуйте снова.")
    if i == password:
        print("Доступ разрешён.")

        
        