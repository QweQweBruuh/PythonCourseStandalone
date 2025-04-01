n = int(input())
s = 0
for o in range(1,n+1):
    count = 0
    for i in range(1,o+1):
        if o % i == 0:
            count +=1
    if count == 2:
        s += i
print(s)