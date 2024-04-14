import sqlite3
import requests

def obtener_datos_sunat(year):
    url = f'https://api.apis.net.pe/v2/sunat/tipo-cambio?year={year}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
        data = response.json()
        return data.get('tc', {})
    except requests.RequestException as e:
        print("Error al consultar la API de SUNAT:", e)
        return None

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        compra REAL,
                        venta REAL
                    )''')
    conn.commit()

def insertar_datos(conn, datos):
    cursor = conn.cursor()
    for fecha, valores in datos.items():
        cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) 
                          VALUES (?, ?, ?)''', (fecha, valores.get('compra'), valores.get('venta')))
    conn.commit()

def mostrar_contenido(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    # Conexión a la base de datos
    conn = sqlite3.connect('base.db')

    # Obtener datos de SUNAT para el año 2023
    datos_2023 = obtener_datos_sunat(2023)
    if datos_2023 is not None:
        # Crear tabla si no existe
        crear_tabla(conn)
        
        # Insertar datos en la tabla
        insertar_datos(conn, datos_2023)

        # Mostrar contenido de la tabla
        print("Contenido de la tabla sunat_info:")
        mostrar_contenido(conn)

    # Cerrar conexión
    conn.close()

if __name__ == "__main__":
    main()
