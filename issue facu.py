import math

def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Seno (sin)")
    print("2. Coseno (cos)")
    print("3. Logaritmo natural (ln)")
    print("4. Potencia (base^exponente)")
    print("5. Salir")
    return input("Selecciona una opción (1-5): ")

def calcular_seno():
    x = float(input("Ingresa el ángulo en radianes: "))
    resultado = round(math.sin(x), 4)
    print(f"sin({x}) = {resultado}")

def calcular_coseno():
    x = float(input("Ingresa el ángulo en radianes: "))
    resultado = round(math.cos(x), 4)
    print(f"cos({x}) = {resultado}")

def calcular_logaritmo():
    x = float(input("Ingresa el número (x > 0): "))
    if x <= 0:
        print("Error: El número debe ser mayor que 0.")
    else:
        resultado = round(math.log(x), 4)
        print(f"ln({x}) = {resultado}")

def calcular_potencia():
    base = float(input("Ingresa la base: "))
    exponente = float(input("Ingresa el exponente: "))
    resultado = round(math.pow(base, exponente), 4)
    print(f"{base}^{exponente} = {resultado}")

# Programa principal
while True:
    opcion = menu()
    
    if opcion == '1':
        calcular_seno()
    elif opcion == '2':
        calcular_coseno()
    elif opcion == '3':
        calcular_logaritmo()
    elif opcion == '4':
        calcular_potencia()
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
