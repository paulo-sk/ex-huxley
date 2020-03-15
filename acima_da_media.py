entrada= []
for x in range(0,3):
    entrada.append(float(input()))

media = sum(entrada) / len(entrada)
count = 0
for x in entrada:
    if x > media:
        count += 1

print(count)

