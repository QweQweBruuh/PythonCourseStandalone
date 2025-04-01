n = int(input())
sum = 0
count = 1
for i in range(1,n+1):
    n = int(input())
    while 0 != n:
      count = n % 10
      n = n // 10
      sum += count
print(sum)    