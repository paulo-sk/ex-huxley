a,b,c,d,e = [float(x)for x in input().split(' ')]
lista_pontos = [a,b,c,d,e]
pontos_invalidos = min(lista_pontos) + max(lista_pontos)
valor_pontuacao = sum(lista_pontos) - pontos_invalidos
print(f"{round(valor_pontuacao,1)}")


