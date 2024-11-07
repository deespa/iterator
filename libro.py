class Libro:
    def __init__(self, titulo: str, autor: str, genero: str):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Género: {self.genero})"
