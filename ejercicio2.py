

def creaLista():  
    numero = []

    for _ in range(7):
        num = int(input("ingresa un numerito:"))
        numero.append(num)
    return numero

variable = creaLista()

print(variable)

def encontrarPositivo(lista):
    seEncontro = False

    for n in lista:
  
     if n > 0 :
    
        seEncontro = True

    if seEncontro:
        return True

    else:
        return False
    

if encontrarPositivo(variable) == True :
    print("se encontro positivo")
else :
    print("no se encontro positivo ")


