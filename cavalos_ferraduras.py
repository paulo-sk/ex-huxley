cavalos = input()
cavalos = int(''.join(c for c in cavalos if c.isdigit()))

ferraduras = cavalos * 4

print(f"Digite a quantidade de cavalos\nSao necessarias {ferraduras} ferraduras")
