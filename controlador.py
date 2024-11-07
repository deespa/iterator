from biblioteca import Biblioteca
from libro import Libro

class Controlador:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def agregar_libros(self):
        libros_iniciales = [
            Libro("1984", "George Orwell", "Ficcion"),
            Libro("El origen de las especies", "Charles Darwin", "Ciencia"),
            Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Ficcion"),
            Libro("Una breve historia del tiempo", "Stephen Hawking", "Ciencia"),
            Libro("La Segunda Guerra Mundial", "Winston Churchill", "Historia"),
            Libro("La primera Guerra Mundial", "Camilo Pardo", "Comedia"),
            Libro("Cronicas de una muerte anunciada", "Gabriel García Márquez", "Ficcion")
            
        ]
        
        for libro in libros_iniciales:
            try:
                self.biblioteca.agregar_libro(libro)
            except ValueError as e:
                print(f"Error al agregar libro {libro.titulo}: {str(e)}")

    def obtener_iterator(self):        
        
        return self.biblioteca.create_iterator() #Retorna un iterator para recorrer todos los libros.

    def obtener_iterator_por_genero(self, genero: str):
        return self.biblioteca.create_filtered_iterator(
            lambda libro: libro.genero.lower() == genero.lower()
        )

    def buscar_por_autor(self, autor: str):
        return self.biblioteca.create_filtered_iterator(
            lambda libro: libro.autor.lower() == autor.lower()
        )

    def buscar_por_titulo(self, titulo: str):
        return self.biblioteca.create_filtered_iterator(
            lambda libro: titulo.lower() in libro.titulo.lower()
        )

    # Métodos de compatibilidad para mantener el código existente funcionando
    def iterar(self):        
        return self.obtener_iterator()

    def iterar_por_genero(self, genero: str):        
        return self.obtener_iterator_por_genero(genero)