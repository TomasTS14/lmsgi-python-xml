class Libro:

    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        #self.autor = autor

    def getISBN(self):
        return self.isbn