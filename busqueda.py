def buscar_en_historial():
    print("\n--- Buscar en historial ---")
    fecha = input("Ingresa la fecha (YYYY-MM-DD) o presiona Enter para omitir: ").strip()
    tipo = input("Ingresa tipo de operación (sin, cos, ln, ^) o presiona Enter para omitir: ").strip()

    try:
        with open("historial.txt", "r") as archivo:
            lineas = archivo.readlines()
            coincidencias = []

            for linea in lineas:
                if fecha and fecha not in linea:
                    continue
                if tipo and tipo not in linea:
                    continue
                coincidencias.append(linea.strip())

            if coincidencias:
                print(f"\nSe encontraron {len(coincidencias)} coincidencias:\n")
                for l in coincidencias:
                    print(l)
            else:
                print("\nNo se encontraron resultados con esos filtros.")
    except FileNotFoundError:
        print("El archivo historial.txt no existe.")
