for a in range(1,1000+1): #1 000 000 копеек = 10 000 рублей
    for b in range(a,1000+1):
        c = 1000 - (a+b)
        if a*a+b*b == c*c:
            print(a,b,c)