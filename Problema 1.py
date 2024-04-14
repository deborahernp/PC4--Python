import requests

def obtener_precio_bitcoin():
    try:
        # Consulta la API de CoinDesk para obtener el precio actual de Bitcoin en USD
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def calcular_valor_bitcoins(n):
    precio_actual = obtener_precio_bitcoin()
    if precio_actual is not None:
        valor_total_usd = n * precio_actual
        return valor_total_usd
    else:
        return None

def main():
    try:
        n = float(input("Ingresa la cantidad de Bitcoins que posees: "))
        valor_total_usd = calcular_valor_bitcoins(n)
        if valor_total_usd is not None:
            print(f"El costo actual de {n:.4f} Bitcoins es ${valor_total_usd:,.4f}")
        else:
            print("No se pudo obtener el precio de Bitcoin. Verifica tu conexión a internet.")
    except ValueError:
        print("Ingresa un valor numérico válido para la cantidad de Bitcoins.")

if __name__ == "__main__":
    main()
