n = int(input())
for i in range(n):
    for j in range(n):
        if j == (n - 1):
            print(min(i+1,j+1,n-i,n-j))
        else:
            print(min(i+1,j+1,n-i,n-j),end = " ")