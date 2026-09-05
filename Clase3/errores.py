# Try: intenta ejecutar el codigo.
# Except: En caso de que el Try no puede ejecutar el codigo, el except evita que rompa el codigo.

try:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    resultado = num1 / num2
    print(resultado)
   
except ZeroDivisionError:
    print("Error: estas dividiendo por cero.")
#except ValueError:
#    print("Error: solo ingresar numeros enteros.")
except Exception as error:
    print (error)
finally:
    print("Fin del programa")
