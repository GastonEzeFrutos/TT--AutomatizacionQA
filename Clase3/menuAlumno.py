# Menu: Registrar alumno, Mostrar alumnos, Mostrar cantidad de alumnos, salir
#1) Nombre, apellido, edad, nota final, porcentaje de asistencia
#2) Recorrer los alumnos registrados y mostrar toda la informacion
#3) mostrar la cantidad alumnos
#4) El programa finaliza cuando ingresa el numero "4"

lista_alumnos = []

while True:
    print("=================================")
    print("Sistema de alumnos")
    print("=================================")
    print("1. Registrar alumno")
    print("2. Mostra alumnos")
    print("3. Mostrar cantidad de alumnos")
    print("4. Salir")
    print("=================================")
    
    opcion = input("Seleccione una opcion: ")
    
    # Registrar alumno
    if opcion == "1":
    
        print("--- REGISTRAR ALUMNO ---")
        nombre = input("Ingrese el nombre: ")
        apellido =  input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        nota = float(input("Ingrese la nota: "))
        asistencia =  int(input("Ingrese el porcentaje de asistencia: "))
        
        # Determinar estado
        if nota >= 7 and asistencia >= 75:
            estado = "Aprobado"
        elif nota >= 4 and asistencia >= 75:
            estado = "Recuperatorio"
        else:
            estado = "Desaprobado"
            
        # Crear diccionario
        alumno = {
            "nombre" : nombre,
            "apellido" : apellido,
            "edad" : edad,
            "nota" : nota,
            "asistencia" : asistencia,
            "estado": estado
        }
        
        lista_alumnos.append(alumno)
        
        print(alumno)
        
        print("Alumno registrado.")
        
    elif opcion == "2":
        print("--- LISTADO DE ALUMNOS ---")
        
        if len(lista_alumnos) == 0:
            print("No hay alumnos registrados")
        else:
            for alumno in lista_alumnos:
                    print("-----------------------")
                    print("Nombre:",alumno["nombre"])
                    print("Apellido:",alumno["apellido"])
                    print("Edad:",alumno["edad"])
                    print("Nota:",alumno["nota"])
                    print("Asistencia:",alumno["asistencia"],"%")
                    print("Estado:",alumno["estado"])

    elif opcion == "3":
        print("--- CANTIDAD DE ALUMNOS ---")
        print("Cantidad de alumnos registrados: ", len(lista_alumnos))
        
    elif opcion == "4":
        print("Programa finalizado...")
        break
    else:
        print("Opcion incorrecta.")
        print("Ingrese una opcion del 1 al 4")
        