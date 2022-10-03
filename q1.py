n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
n3 = float(input('Digite sua 3° nota: '))

media = (n1 + n2 + n3) / 3
print('Sua Média foi: ',  media)

if media == 10:
    print('Aprovado com distinção !!')
elif media >= 7 and media < 10:
    print('Aprovado !!')
else:
    print('Reprovado !!')