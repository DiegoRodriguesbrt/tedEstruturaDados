def reverso(numero):
    
    return str(numero[:: -1])

numero = str(input("Digite um número: ")).strip()

print(reverso(numero))