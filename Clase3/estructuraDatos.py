lista = ["Manzana", "Banana", "Durazno"] # Se puede incluir distintos tipos de datos: enteros, fraccion, string, bool, etc.
tupla = (1,2,3,4,5) # Es como una constante, no se puede modificar.

lista.append("Melon") # Agrega elementos a la lista
lista.remove("Banana") # Elimina elementos de la lista
lista.pop(0) # Elimina elementos de la lista segun el indice
lista.insert(1,"Frutilla") # Agrega elementos a la lista en el indice que se quiera

print (lista)

persona = {
    "nombre": "Gaston",
    "edad": 28,
    "pais": "Argentina",
    "altura":1.72
} # Esto es un diccionario, tiene clave - valor

persona ["edad"] = 25 # Para actualizar el diccionario
persona ["apellido"] ="Frutos" # Para agregar directamente el diccionario

del persona ["altura" ] # Para eliminar una clave del diccionario

for clave,valor in persona.items():
    print(clave,valor)
