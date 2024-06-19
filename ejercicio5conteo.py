def creaLista():  
    temperatura = []

    for i in range(6):
        dias = float(int(input("ingresa un numerito:")))
        dias.append(dias)
    return dias 

variable = creaLista()
print(variable)

def seEncontroDiasFrios(lista):
    diasFrios = 0 

    for temp in lista:
  
     if temp <= -10 and temp >= 5 :
    
        diasFrios = diasFrios + 1

     
    return diasFrios

    

if seEncontroDiasFrios(variable) :
    print("se encontraron dias frios")
else :
    print("no se encontraron dias frios")
