n = int(input())
s = 0    
for i in range(0,n):
    for o in range(0,i+1):
       o = f"{o}"
       s += 1
       print(o,end = '')
    print()
             