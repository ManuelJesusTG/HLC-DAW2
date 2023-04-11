import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.filmaffinity.com/es/film576352.html")

respuesta = open("respuesta.html","w")

respuesta.write(html.text)

texto = html.text

sopa = BeautifulSoup(html.text,"html.parser")

def titulo_o():
    titulo = texto[texto.find("<dt>Título original</dt>"):texto.find("</dd>")]
    resultado = titulo[titulo.find("<dd>"):].splitlines()[1]
    resultado = resultado.lstrip().rstrip()
    AKA = resultado.find('<span')
    if (AKA != -1):
        resultado = resultado[:AKA]
    return resultado


def anio():
    anio = texto[texto.find('<dd itemprop="datePublished">'):texto.find('<dt>Duración</dt>')]

    # A partir de aqui empiezo a usar BeautifulSoup

    otro = sopa.find('dd', {'itemprop' : 'datePublished'}).getText()
    
    return otro


def duracion(): 
    duracion = sopa.find('dd', {'itemprop' : 'duration'}).getText()

    return duracion

def pais():
    pais = texto[texto.find("<dt>País</dt>"):texto.find("<dt>Dir")]
    resultado = BeautifulSoup(pais,"html.parser")
    resultado = resultado.find('dd').getText()

    return resultado

def direccion():
    direccion = sopa.find('div', {'class' : 'credits'}).getText()

    return direccion

def guion():
    guion = texto[texto.find("<dt>Guion</dt>"):texto.find("<dt>Música")]
    resultado = BeautifulSoup(guion,"html.parser")
    resultado = resultado.find('div', {'class' : 'credits'}).getText()

    return resultado

def musica():
    musica = texto[texto.find("<dt>Música</dt>"):texto.find("<dt>Foto")]
    resultado = BeautifulSoup(musica,"html.parser")
    resultado = resultado.find('div', {'class' : 'credits'}).getText()
    #resultado = musica[musica.find("<dt>"):].splitlines()[1]
    #resultado = resultado.lstrip().rstrip()
    #resultado = resultado.find('div', {'class' : 'credits'}).getText()

    return resultado

def fotografia():
    fotografia = texto[texto.find("<dt>Foto"):texto.find("<dt>Repar")]
    resultado = BeautifulSoup(fotografia,"html.parser")
    resultado = resultado.find('div', {'class' : 'credits'}).getText()

    return resultado

def reparto():
    reparto = sopa.find('dd', {'class' : 'card-cast'}).getText()
    reparto = reparto.lstrip().rstrip()

    return reparto

def productora():
    productora = sopa.find('dd', {'class' : 'card-producer'}).getText()
    productora = productora.lstrip().rstrip()

    return productora

def genero(): 
    genero = sopa.find('dd', {'class' : 'card-genres'}).getText()
    genero = genero.lstrip().rstrip()


    return genero

def sinopsis():
    sinopsis = sopa.find('dd', {'itemprop' : 'description'}).getText()

    return sinopsis


diccionario = dict(Titulo=titulo_o(),Año=anio(),Duracion=duracion(),pais=pais(),Direccion=direccion(),Guion=guion(),Musica=musica(),Fotografia=fotografia(),Reparto=reparto(),Productora=productora(),Genero=genero(),Sinopsis=sinopsis())

print(guion())
print(diccionario)