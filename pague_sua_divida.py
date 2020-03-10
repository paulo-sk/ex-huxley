divida = int(input())
parcela = int(input())

if parcela > divida:
    print(f"(antes) {divida}")
    print(f"(depois) {0}")

else:

    if divida % parcela == 0:
        tempo = divida / parcela
    else:
        tempo = int(round(divida/parcela + 1, 0))

    x = 0
    while x < tempo:
        print(f"(antes) {divida}")
        divida -= parcela
        print(f"(depois) {divida}")
        x += 1
        