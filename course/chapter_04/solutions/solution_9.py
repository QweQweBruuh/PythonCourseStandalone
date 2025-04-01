f1= int(input())
f2= int(input())
Fn = 0
print(f1)
print(f2)
n = int(input())
for i in range(0,n-2):
    Fn = f1 + f2
    print(Fn)
    f1 = f2
    f2 = Fn