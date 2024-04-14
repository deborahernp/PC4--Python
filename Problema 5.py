def guardar_tabla_multiplicar(numero):
    try:
        nombre_fichero = f"tabla-{numero}.txt"
        with open(nombre_fichero, 'w') as archivo:
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")
        print(f"Tabla de multiplicar del {numero} guardada en {nombre_fichero}")
    except Exception as e:
        print(f"Error al guardar la tabla: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        nombre_fichero = f"tabla-{numero}.txt"
        with open(nombre_fichero, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"No existe el fichero con la tabla del {numero}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        nombre_fichero = f"tabla-{numero}.txt"
        with open(nombre_fichero, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1])
            else:
                print(f"La línea {linea} no existe en el fichero")
    except FileNotFoundError:
        print(f"No existe el fichero con la tabla del {numero}")

if __name__ == '__main__':
    try:
        opcion = int(input("Seleccione una opción:\n1. Guardar tabla de multiplicar\n2. Mostrar tabla de multiplicar\n3. Mostrar línea específica\n"))
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        if opcion == 1:
            guardar_tabla_multiplicar(numero)
        elif opcion == 2:
            mostrar_tabla_multiplicar(numero)
        elif opcion == 3:
            linea = int(input("Introduce el número de línea a mostrar: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        else:
            print("Opción no válida")
    except ValueError:
        print("Por favor, introduce un número entero válido.")
