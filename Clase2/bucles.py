# Bucle for
lista = ["De Paul", "Messi", "Tevez"]
for jugador in lista:
    print(jugador)

print(len(lista))
print(len("Diego Milito"))

for numero in range(5): #0,1,2,3,4
    print(numero)


for letra in "Diego Milito":
    print(letra)

# Acumulador

lista_precios = [2000, 2000, 5200, 7000]

total = 0

for precio in lista_precios:
    total = total + precio
    print(total)

# Bucle While
contador = 0
while contador < 5:
    print(contador)
    contador += 1

contraseña = ""
contador_contraseña = 0

while contraseña != "1234" and contador_contraseña < 3:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "1234":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta, intente nuevamente.")
        contador_contraseña += 1

    if contador_contraseña == 3:
        print("Llegaste al limite de intentos, intente más tarde.")

# Break

sumatoria = 0

while sumatoria < 10:
    print(sumatoria)
    if sumatoria == 3:
        break
    sumatoria = sumatoria + 1

# Continue

contador_2 = 0

while contador_2 < 5:
    contador_2 += 1
    if contador_2 == 3:
        continue
    print (contador_2)