nota = float(input("Informe uma nota de 0 a 10:"))

while(nota < 0 or nota > 10):
    
    print("Nota inválida. Digite novamente, por favor !")
    
    nota = float(input("Informe uma nota de 0 a 10:"))

print("Nota escolhida: ", nota)
