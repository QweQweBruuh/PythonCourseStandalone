n = int(input())
s = 0    
for i in range(n):
    for o in range(n,i,-1):
       o = f"{o}"
       s += 1
       print(o,end = '')
    print()
             
       