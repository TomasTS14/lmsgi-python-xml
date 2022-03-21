from utils import read,write
from libro import Libro

listaLibros=[]

def agregar_a_Lista():
    libreria = read('datos/libros.xml')
    for libro in libreria:
        attribISBN = libro.attrib['isbn']
        attribTitulo = libro.find('titulo')
        libroAux = Libro(attribISBN,attribTitulo)
        listaLibros.append(libroAux)

agregar_a_Lista()
print(listaLibros)