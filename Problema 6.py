def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.lower().endswith(".py"):
            print("El archivo debe tener extensión .py")
            return

        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()

            # Filtrar líneas en blanco y comentarios
            lineas_codigo = [linea for linea in lineas if linea.strip() and not linea.strip().startswith("#")]

            print(f"El archivo '{ruta_archivo}' tiene {len(lineas_codigo)} líneas de código.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}'.")

# Solicitar al usuario la ruta del archivo
ruta_archivo = input("Ingresa la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
