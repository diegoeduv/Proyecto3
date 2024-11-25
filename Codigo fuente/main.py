modalidad = input("Ingrese la modadlidad: ")
if modalidad == "c":
    archivoEvaluaciones = input("Ingrese el nombre del archivo donde serán guardadas las n evaluaciones del polinomio: ")
    evaluaciones = int(input("Ingrese el número de evaluaciones que se realizarán: "))
    minimos = int(input("Ingrese el número de mínimo de punto necesarios para descifrar: "))
    archivo = "Ingrese el nombre del archivo que se desea cifrar"
    contraseña = input("Ingrese una contraseña: ")
    cifrar(nombre_evaluaciones, evaluaciones, minimos, archivo, contraseña)
elif modalidad == "d":
    archivoEvaluaciones = input("Ingrese el nombre del archivo con al menos 't' de las  'n' evaluaciones: ")
    archivoAES = input("Ingrese el nombre del archivo cifrado: ")
    descifrar(archivoAES, archivoEvaluaciones)
