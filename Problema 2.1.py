import random
from pyfiglet import Figlet

def obtener_fuente_aleatoria():
    # Obtiene una fuente aleatoria de la lista de fuentes disponibles
    f = Figlet()
    fuentes_disponibles = f.getFonts()
    return random.choice(fuentes_disponibles)

def main():
    try:
        fuente_seleccionada = input("Ingresa el nombre de la fuente (deja en blanco para aleatoria): ")
        if not fuente_seleccionada:
            fuente_seleccionada = obtener_fuente_aleatoria()

        texto_imprimir = input("Ingresa el texto que deseas renderizar: ")

        f = Figlet()
        f.setFont(font=fuente_seleccionada)
        resultado = f.renderText(texto_imprimir)

        print(resultado)
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")

if __name__ == "__main__":
    main()
