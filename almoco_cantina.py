# lasanha = 8 reais
# estrogonofe = 11 reais

# refri = 3 reais
# suco = 2,50 reais

alomoco = input()
bebida = input()

conta = 0

if alomoco.lower() == 'lasanha':
    conta += 8
elif alomoco.lower() == 'estrogonofe':
    conta += 11

if bebida.lower() == 'suco':
    conta += 2.5
elif bebida.lower() == 'refrigerante':
    conta += 3

print(f"{conta:.2f}")
