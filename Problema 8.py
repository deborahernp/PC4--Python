import sqlite3
import requests

def obtener_precio_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
        data = response.json()
        return data.get('bpi', {}).get('USD', {}).get('rate_float')
    except requests.RequestException as e:
        print("Error al consultar la API de Bitcoin:", e)
        return None

def obtener_tipo_cambio_sunat():
    url = 'https://api.apis.net.pe/v2/sunat/tipo-cambio'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
        data = response.json()
        tipo_cambio = data.get('tc', {}).get('venta', {}).get('USD')
        return tipo_cambio
    except requests.RequestException as e:
        print("Error al consultar la API de SUNAT:", e)
        return None

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_usd REAL,
                        tipo_cambio_pen REAL,
                        tipo_cambio_eur REAL
                    )''')
    conn.commit()

def insertar_datos(conn, precio_usd, tipo_cambio_pen, tipo_cambio_eur):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, tipo_cambio_pen, tipo_cambio_eur) 
                      VALUES (DATE('now'), ?, ?, ?)''', (precio_usd, tipo_cambio_pen, tipo_cambio_eur))
    conn.commit()

def calcular_precio_en_moneda(bitcoins, tipo_cambio):
    return bitcoins * tipo_cambio

def consultar_base_datos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    row = cursor.fetchone()
    return row

def main():
    # Conexión a la base de datos
    conn = sqlite3.connect('base.db')

    # Obtener precio del Bitcoin en USD
    precio_usd = obtener_precio_bitcoin()
    if precio_usd is None:
        print("No se pudo obtener el precio del Bitcoin en USD.")
        return

    # Obtener tipo de cambio de SUNAT
    tipo_cambio_pen = obtener_tipo_cambio_sunat()
    if tipo_cambio_pen is None:
        print("No se pudo obtener el tipo de cambio de PEN.")
        return

    tipo_cambio_eur = tipo_cambio_pen  # Suponiendo que el tipo de cambio de EUR es el mismo que el de PEN

    # Crear tabla si no existe
    crear_tabla(conn)

    # Insertar datos en la tabla
    insertar_datos(conn, precio_usd, tipo_cambio_pen, tipo_cambio_eur)

    # Consultar la base de datos para obtener los datos más recientes
    row = consultar_base_datos(conn)
    if row is not None:
        precio_pen = calcular_precio_en_moneda(10, row[2])
        precio_eur = calcular_precio_en_moneda(10, row[3])
        print(f"Precio de comprar 10 bitcoins en PEN: {precio_pen}")
        print(f"Precio de comprar 10 bitcoins en EUR: {precio_eur}")

    # Cerrar conexión
    conn.close()

if __name__ == "__main__":
    main()
