n = int(input())
count = 1
while n < 0:
    n = int(input())
while count <= n:
    if n % count == 0:
        print(count)
    count += 1
