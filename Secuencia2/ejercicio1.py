from calendar import leapdays

año1 = int(input("Año 1: "))
año2 = int(input("Año 2: ") )


while año1 > año2:
    print("el primer año debe ser menor que el segundo")
    año1 = int(input("Año 1: "))
    año2 = int(input("Año 2:  "))

else :
    print(f"Entre {año1} y {año2} hay {leapdays(año1, año2)} años bisiestos")