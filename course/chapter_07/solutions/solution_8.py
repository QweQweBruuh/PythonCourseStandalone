names = []
urodi = []
new = []
itog = []
n = input()
while n != '':
    names.append(n)
    n = input()
e = input()
while e != '':
    names.append(e)
    e = input()
a = input()
while a != '':
    urodi.append(a)
    a = input()
for i in names:
    for o in urodi:
        if i == o:
           names.remove(i)
print(names)