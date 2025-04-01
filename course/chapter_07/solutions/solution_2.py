numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chet = []
nechet = []
for i in numbers:
    if i % 2 == 0:
        chet.append(i)
    if i % 2 != 0:
        nechet.append(i)
print(*chet,sep = ', ')
print(*nechet,sep = ', ')        
   



