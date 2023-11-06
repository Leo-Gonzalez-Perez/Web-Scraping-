import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")

# Obtener un str con el contenido de resultado
#print(resultado.text)

# Pero lo que necesitamos es el contenido en un tipo de objeto que nos permita hacer scraping, y eso lo permitira sopa
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)
#print(sopa.select("title")[0].getText())
#print(len(sopa.select("li")))

titulos = sopa.select('.r-snippetized')
for t in titulos:
    print(t.getText())

# post_titles = soup.find_all("h3", class_="post-title")
