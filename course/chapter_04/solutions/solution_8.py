f1=1
f2=1
Fn = 0
n = int(input())
print("Числа Фибоначчи:")
print(f1)
print(f2)
for i in range(0,n-2):
    Fn = f1 + f2
    print(Fn)
    f1 = f2
    f2 = Fn
   