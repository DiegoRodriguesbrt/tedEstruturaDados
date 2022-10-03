numero = int(input("Digite um número inteiro: "))

lista = []

print(numero)

for i in range(numero + 1):
     if i % 2 == 1 and i != 2:
         lista.append(i)


print(lista)