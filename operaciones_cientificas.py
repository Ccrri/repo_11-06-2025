# funciones matemáticas
def calcular_seno():
    x = float(input("Ingresa el ángulo en radianes: "))
    resultado = round(math.sin(x), 4)
    operacion = f"sin({x}) = {resultado}"
    print(operacion)
    guardar_en_archivo(operacion)

def calcular_coseno():
    x = float(input("Ingresa el ángulo en radianes: "))
    resultado = round(math.cos(x), 4)
    operacion = f"cos({x}) = {resultado}"
    print(operacion)
    guardar_en_archivo(operacion)

def calcular_logaritmo():
    x = float(input("Ingresa el número (x > 0): "))
    if x <= 0:
        print("Error: El número debe ser mayor que 0.")
    else:
        resultado = round(math.log(x), 4)
        operacion = f"ln({x}) = {resultado}"
        print(operacion)
        guardar_en_archivo(operacion)

def calcular_potencia():
    base = float(input("Ingresa la base: "))
    exponente = float(input("Ingresa el exponente: "))
    resultado = round(math.pow(base, exponente), 4)
    operacion = f"{base}^{exponente} = {resultado}"
    print(operacion)
    guardar_en_archivo(operacion)

# ver historial de la sesión actual
def ver_historial():
    print("\n--- Historial de operaciones (sesión actual) ---")
    if not historial:
        print("No hay operaciones registradas.")
    else:
        for i, op in enumerate(historial, 1):
            print(f"{i}. {op}")

# ver historial completo desde archivo
def ver_historial_archivo():
    print("\n--- Historial completo desde archivo ---")
    try:
        with open("historial.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print("El archivo está vacío.")
    except FileNotFoundError:
        print("No se encontró el archivo historial.txt.")

# recuperar operación por expresión exacta
def recuperar_operacion():
    expresion = input("\nIngresa la operación exacta a recuperar (ej: ln(10.0)): ").strip()
    try:
        with open("historial.txt", "r") as archivo:
            coincidencias = [linea.strip() for linea in archivo if expresion in linea]
        if coincidencias:
            print("\nÚltima coincidencia encontrada:")
            print(coincidencias[-1])
        else:
            print("No se encontró ninguna operación con esa expresión.")
    except FileNotFoundError:
        print("El archivo historial.txt no existe.")

# borrar historial.txt
def borrar_historial_archivo():
    if os.path.exists("historial.txt"):
        confirmacion = input("¿Estás seguro que deseas borrar el historial? (s/n): ").lower()
        if confirmacion == "s":
            os.remove("historial.txt")
            print("Archivo historial.txt borrado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No existe un archivo historial.txt para borrar.")

# función que guarda historial de operaciones con fecha
def guardar_en_archivo(operacion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] {operacion}"
    with open("historial.txt", "a") as archivo:
        archivo.write(linea + "\n")
    historial.append(linea)