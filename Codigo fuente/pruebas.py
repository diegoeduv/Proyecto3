import os
import sys
import cifrar
import  descifrar

def prueba_polinomio():
    # Prueba de la función generar_polinomio
    print("Prueba de la función generar_polinomio")
    polinomio = cifrar.generar_polinomio(5)
    print("Coeficientes para el polinimio generados: ", polinomio)

def prueba_evaluacion_polinomio():
    # Prueba de la función evaluacion_polinomio
    print("Prueba de la función evaluacion_polinomio")
    polinomio = cifrar.generar_polinomio(5)
    print("Coeficientes para el polinimio generados: ", polinomio)
    clave = 5
    x = 6
    resultado = cifrar.evaluacion_polinomio(polinomio, clave, x)
    print("Resultado de la evaluación del polinomio: ", resultado)

def prueba_cifrar():
    # Prueba de la función cifrar
    print("Prueba de la función cifrar")
    archivo_evaluaciones = "evaluaciones.txt"
    evaluaciones = 2
    minimos = 5
    archivo = "texto_plano.txt"
    contraseña = "contraseña"
    cifrar.cifrar(archivo_evaluaciones, evaluaciones, minimos, archivo, contraseña)
    print("Archivo cifrado")

prueba_polinomio()
prueba_evaluacion_polinomio()