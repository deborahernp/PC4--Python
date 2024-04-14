import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raises an exception for 4xx and 5xx status codes
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print("Error al consultar la API:", e)
        return None

def write_to_file(bitcoin_price, filename):
    try:
        with open(filename, 'w') as file:
            file.write(f"Precio actual de Bitcoin: ${bitcoin_price:,.4f}")
        print("Datos almacenados en", filename)
    except IOError as e:
        print("Error al escribir en el archivo:", e)

def main():
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        write_to_file(bitcoin_price, 'bitcoin_price.txt')

if __name__ == "__main__":
    main()
