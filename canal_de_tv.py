#  2=SBT, 4=BAND, 6=RedeTV!, 9=Record,13=Globo.
# saida:
# Digite um numero de um canal de tv:
# REDETV!

canal = int(input())

if canal == 2:
    print("Digite um numero de um canal de tv:\nSBT")
elif canal == 4:
    print("Digite um numero de um canal de tv:\nBAND")
elif canal == 6:
    print("Digite um numero de um canal de tv:\nREDETV!")
elif canal == 9:
    print("Digite um numero de um canal de tv:\nRECORD")
elif canal == 13:
    print("Digite um numero de um canal de tv:\nGLOBO")
else:
    print("Digite um numero de um canal de tv:\nCanal Invalido")