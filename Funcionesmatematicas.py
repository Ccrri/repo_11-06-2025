import math

def mostrar_menu():
    print("\n--- CALCULADORA AVANZADA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia (x^y)")
    print("6. Raíz cuadrada")
    print("7. Raíz enésima")
    print("8. Logaritmo base 10")
    print("9. Logaritmo natural (ln)")
    print("10. Funciones trigonométricas (sen, cos, tan)")
    print("11. Evaluar expresión matemática")
    print("0. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break

        elif opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a + b}")

        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a - b}")

        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a * b}")

        elif opcion == "4":
            a = float(input("Dividendo: "))
            b = float(input("Divisor: "))
            if b != 0:
                print(f"Resultado: {a / b}")
            else:
                print("Error: División por cero")

        elif opcion == "5":
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            print(f"Resultado: {math.pow(base, exponente)}")

        elif opcion == "6":
            x = float(input("Número: "))
            if x >= 0:
                print(f"Resultado: {math.sqrt(x)}")
            else:
                print("Error: No se puede sacar raíz de número negativo")

        elif opcion == "7":
            x = float(input("Número: "))
            n = float(input("Índice de la raíz: "))
            if x >= 0 or int(n) % 2 != 0:
                print(f"Resultado: {x ** (1/n)}")
            else:
                print("Error: Raíz inválida para número negativo")

        elif opcion == "8":
            x = float(input("Número: "))
            if x > 0:
                print(f"Resultado: {math.log10(x)}")
            else:
                print("Error: Logaritmo de número no positivo")

        elif opcion == "9":
            x = float(input("Número: "))
            if x > 0:
                print(f"Resultado: {math.log(x)}")
            else:
                print("Error: Logaritmo de número no positivo")

        elif opcion == "10":
            angulo = float(input("Ángulo en grados: "))
            rad = math.radians(angulo)
            print(f"sen({angulo}°) = {math.sin(rad)}")
            print(f"cos({angulo}°) = {math.cos(rad)}")
            print(f"tan({angulo}°) = {math.tan(rad)}")

        elif opcion == "11":
            expr = input("Ingresá la expresión matemática (ej: sin(45) + log(10)): ")
            try:
                resultado = eval(expr, {"__builtins__": None}, {
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "tan": lambda x: math.tan(math.radians(x)),
                    "log": math.log10,
                    "ln": math.log,
                    "sqrt": math.sqrt,
                    "pow": math.pow,
                    "pi": math.pi,
                    "e": math.e
                })
                print(f"Resultado: {resultado}")
            except Exception as e:
                print("Error en la expresión:", e)

        else:
            print("Opción inválida")

if __name__ == "__main__":
    calculadora()