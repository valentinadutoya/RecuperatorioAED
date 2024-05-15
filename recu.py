numero = []

for _ in range(4):
 num = int(input("ingresa un numerito:"))
 numero.append(num)
print(f"{numero}")

seEncontro = False

for n in numero:
  if n > 0 :
    seEncontro = True

if seEncontro:
  print("se encontro un positivo")
else:
  print("ñao ñao ") 