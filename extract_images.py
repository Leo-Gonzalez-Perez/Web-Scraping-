import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

url_imagen_1 = sopa.select(".course-box-image")[0]["src"]

imagen_curso_1 = requests.get(url_imagen_1)

fd_imagen_1 = open("imagen_numero_1.jpg", "wb")
fd_imagen_1.write(imagen_curso_1.content)
fd_imagen_1.close