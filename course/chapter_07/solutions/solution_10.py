a = []
b = []
c = []
d = []
x = input()
while x != '':
    a.append(x)
    x = input()
y = input()
while y != '':
    a.append(y)
    y = input()
z = input()
while z != '':
    b.append(z)
    z = input()
    for i in b:
        for o in a:
            if i == o:
               a.remove(o) 
else:
    print("такой игрушки нет")
    
print(a)

    