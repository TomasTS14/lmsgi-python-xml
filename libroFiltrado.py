from utils import *
import xml.etree.ElementTree

def  sacarTodos():
    contentXML = '<libreria>'
    libreria = read('datos/libros.xml')
    tipoLibro = libreria.find('libro').tag
    for libro in libreria:
    
        atribISBN = libro.attrib['isbn']
        contentXML += f'<{tipoLibro} isbn={atribISBN}>'
    contentXML += '</libreria>'
    write('todosISBN.xml',contentXML)

sacarTodos()

#def pasarALista()