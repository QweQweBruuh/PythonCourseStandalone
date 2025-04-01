sum = 0
count = 0
while count != 5:
    a = int(input())
    if a > 0:
        count += 1
    if a < 0:
        continue
    sum += a
print(sum)
