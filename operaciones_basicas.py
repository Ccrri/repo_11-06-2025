def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")

    while True:
        try:
            opcion = input("\nSelecciona una operación (1-5): ")
            
            if opcion == '5':
                print("¡Hasta luego!")
                break
            
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Opción no válida. Intenta de nuevo.")
        
        except ValueError:
            print("Error: Ingresa números válidos.")

if __name__ == "__main__":
    calculadora()