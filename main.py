import math
import os
from datetime import datetime
from busqueda import buscar_en_historial
import suma
import resta
import multiplicacion
import division

historial = []

# función para ver menú
def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("1. Seno (sin)")
    print("2. Coseno (cos)")
    print("3. Logaritmo natural (ln)")
    print("4. Potencia (base^exponente)")
    print("5. Ver historial (sesión actual)")
    print("6. Ver historial completo desde archivo")
    print("7. Salir")
    print("8. Buscar en historial por fecha y/u operación")
    print("9. Recuperar operación por expresión exacta")
    print("10. Borrar historial completo")
    return input("Selecciona una opción (1-10): ")


# programa principal
while True:
    opcion = menu()

    if opcion == '1':
        suma()
    elif opcion == '2':
        resta()
    elif opcion == '3':
        multiplicacion()
    elif opcion == '4':
        division()
    # elif opcion == '5':
    #     ver_historial()
    # elif opcion == '6':
    #     ver_historial_archivo()
    # elif opcion == '7':
    #     print("Saliendo del programa.")
    #     break
    # elif opcion == '8':
    #     buscar_en_historial()
    # elif opcion == '9':
    #     recuperar_operacion()
    # elif opcion == '10':
    #     borrar_historial_archivo()
    else:
        print("Opción no válida. Intenta nuevamente.")
