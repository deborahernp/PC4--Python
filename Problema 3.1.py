import requests

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada como {filename}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

if __name__ == '__main__':
    image_url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    image_filename = "my_image.jpg"
    download_image(image_url, image_filename)

import zipfile

def create_zip(filename, image_filename):
    try:
        with zipfile.ZipFile(filename, 'w') as zip_file:
            zip_file.write(image_filename)
        print(f"Imagen comprimida en {filename}")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

if __name__ == '__main__':
    zip_filename = "my_image.zip"
    create_zip(zip_filename, image_filename)

def unzip(filename, output_dir):
    try:
        with zipfile.ZipFile(filename, 'r') as zip_file:
            zip_file.extractall(output_dir)
        print(f"Imagen descomprimida en {output_dir}")
    except Exception as e:
        print(f"Error al descomprimir el archivo ZIP: {e}")

if __name__ == '__main__':
    output_directory = "unzipped_images"
    unzip(zip_filename, output_directory)
