idades = []

alturas = []

for i in range(1 , 6):
    
    print('%dº Pessoa' % i)
    
    idade = int(input("Informe sua idade: "))
    
    altura = float(input("Informe sua altura: "))
    
    idades.append(idade)
    
    alturas.append(altura)


print("\nOrdem inversa das idades:")

print(idades[:: -1])

print("\nOrdem inversa das alturas:")

print(alturas[:: -1])