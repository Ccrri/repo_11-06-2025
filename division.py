def division():
    a = float(input("Dividendo: "))
    b = float(input("Divisor: "))
    if b != 0:
        print(f"Resultado: {a / b}")
    else:
        print("Error: División por cero")