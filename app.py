from flask import Flask, jsonify
from controlador import Controlador

app = Flask(__name__)

# Inicializamos el controlador y agregamos los libros
controlador = Controlador()
controlador.agregar_libros()

@app.route("/")
def home():
    return "<h1>Bienvenido a la Biblioteca</h1><p>Usa las rutas /libros para ver todos los libros o /libros/<genero> para ver libros de un género específico.</p>"

@app.route("/libros", methods=["GET"])
def obtener_libros():
    libros = []
    iterator = controlador.biblioteca.iterar()  # Debería devolver todos los libros
    while iterator.has_next():
        libro = iterator.next()
        libros.append({
            "titulo": libro.titulo,
            "autor": libro.autor,
            "genero": libro.genero
        })
    return jsonify(libros)

@app.route("/libros/<genero>", methods=["GET"])
def obtener_libros_por_genero(genero):
    libros_genero = []
    iterator_genero = controlador.biblioteca.iterar_por_genero(genero.capitalize())  # Filtra por género
    while iterator_genero.has_next():
        libro = iterator_genero.next()
        libros_genero.append({
            "titulo": libro.titulo,
            "autor": libro.autor,
            "genero": libro.genero
        })
    return jsonify(libros_genero)

if __name__ == "__main__":
    app.run(port=5000)
