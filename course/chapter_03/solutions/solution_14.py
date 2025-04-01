n = int(input())
count = 1
sum = 0
while n < 0:
    n = int(input())
while 0 != n:
    count = n % 10
    n = n // 10
    sum += count
print(sum)