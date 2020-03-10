a,b = [int(x) for x in input().split(' ')]
count = 0
for x in range(0,a):
    numero = int(input())
    if numero == b:
        count += 1

print(count)