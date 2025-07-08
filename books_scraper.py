import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL base del sitio de prueba para scraping
url = 'http://books.toscrape.com/'

# Hacer la solicitud a la página
response = requests.get(url)

# Analizar el contenido HTML usando BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar todos los bloques que contienen productos (libros)
books = soup.find_all('article', class_='product_pod')

# Lista vacía para almacenar los datos extraídos
data = []

# Recorrer cada producto y extraer la información deseada
for book in books:
    # Título del libro (está en el atributo title del enlace)
    title = book.h3.a['title']

    # Precio del libro (dentro de un <p class="price_color">)
    price = book.find('p', class_='price_color').get_text(strip=True)

    # Disponibilidad (si está en stock o no)
    availability = book.find('p', class_='instock availability').get_text(strip=True)

    # Calificación en estrellas (por clase CSS como "star-rating Three")
    rating_class = book.p['class'][1]  # Ejemplo: ['star-rating', 'Three']
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    rating = rating_map.get(rating_class, 0)  # Convertimos texto a número

    # Enlace al detalle del producto (relativo a la URL base)
    link = url + book.h3.a['href']

    # Guardar los datos en un diccionario y agregarlo a la lista
    data.append({
        'title': title,
        'price': price,
        'availability': availability,
        'rating': rating,
        'link': link
    })

# Crear un DataFrame con Pandas
df = pd.DataFrame(data)

# Exportar el resultado a un archivo Excel
df.to_excel('books.xlsx', index=False)

print("✅ Archivo 'books.xlsx' generado exitosamente.")
