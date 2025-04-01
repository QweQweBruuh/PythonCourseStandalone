n = int(input())
count = 1
sum = 0
while 0 != n:
   count = n % 10
   n = n // 10
   sum += count
print(sum)
