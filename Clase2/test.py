print("¡Hola automatation test!")

nombre = input("¿Cual es tu nombre? ")

print (f"Hola, {nombre}")

edad = int(input("¿Cual es tu edad? "))
altura = float(input("Ingresa tu altura: "))

print(f"Tenes, {edad} años y tu altura es {altura}")

if edad >= 18:
    print("Podes trabajar en TalentoLab")
elif edad >= 16:
    print("Hace mejor una pasantia.")
else:
    print("Sos menor de edad, no podes trabajar.") 


for i in range (5) :
    print(i)

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1


suma = 0

for b in range (1, 11):
    suma += b
    print (f"La suma es: {suma}")


for c in range (10):
    if c == 5:
        break
    print (c)

for d in range (5):
    if d == 2:
        continue
    print (d)