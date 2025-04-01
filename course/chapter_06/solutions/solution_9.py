r = int(input())
c = int(input())
n_max = r*c
l = len(str(n_max))
for i in range( 1,r+1):
    for j in range(i,n_max+1,r):
        l1 = len(str(j))
        space = (l-l1+1) * " "
        if (n_max - j) >= r: #(n_max - j) < r
            print(j,end = space)
        else:
            print(j,end = "")
    print()