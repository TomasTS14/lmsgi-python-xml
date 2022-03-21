from utils import *
import xml.etree.ElementTree

def  sacarTodos():
    contentXML = '<libreria>'
    libreria = read('datos/libros.xml')
    for libro in libreria:
        tipoLibro = libreria.find('libro').tag
        atribISBN = libro.attrib['isbn']
        contentXML += f'<{tipoLibro} isbn={atribISBN}>'
    contentXML += '</libreria>'
    write('todosISBN.xml',contentXML)

sacarTodos()

#def pasarALista()