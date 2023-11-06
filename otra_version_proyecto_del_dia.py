import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
titulos_rating_alto = []

for pagina in range(1, 51):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    libros = sopa.select('.product_pod')
    for libro in libros:
        price_element = libro.find('p', class_='price_color')
        if price_element:
            price_text = price_element.text
            # Removemos caracteres no numéricos y obtenemos solo los dígitos y el punto decimal
            numeric_value = ''.join(filter(str.isdigit, price_text + '.'))
            # Convertimos el valor a un número en punto flotante (float)
            numeric_value_float = float(numeric_value)
            print("Valor numérico:", numeric_value_float)
        else:
            print("Precio no encontrado para este libro")