from typing import Union
from fastapi import FastAPI, UploadFile
from Model.Film import Film
from db import clientPM
from db import filmDB

# Crear instancia de la aplicación FastAPI
app = FastAPI()

# Conectar con la base de datos al iniciar la aplicación
conn = clientPM.dbFilms()

# Ruta raíz, retorna un mensaje de bienvenida
@app.get("/")
def red_root():
    clientPM.dbFilms()  # Conectar a la base de datos
    return {"Hello": "World"}

# Ruta para obtener todos los films
@app.get("/films")
def getProducts():
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.consulta()  # Consultar todos los films
    return data

# Ruta para filtrar films por género, por defecto es "Comedy"
@app.get("/filmsGenere")
def getProducts(genere: str = "Comedy"):
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.consultaGenere(genere)  # Consultar films por género
    return data

# Ruta para ordenar films por un campo específico, por defecto es "title" en orden ascendente
@app.get("/filmsOrder")
def getProducts(field: str = "title", order: str = "asc"):
    clientPM.dbFilms()  # Conectar a la base de datos
    # Convertir el parámetro de orden a la orden de ordenamiento de MongoDB
    mongo_order = 1 if order == "asc" else -1
    data = filmDB.consultaOrder(field, mongo_order)  # Consultar films ordenados
    return data

# Ruta para limitar el número de films retornados, por defecto 10
@app.get("/filmsLimit")
def consultaLimit(limit: int = 10):
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.consultaLimit(limit)  # Consultar films con límite
    return data

# Ruta para obtener un film por su ID
@app.get("/film/{id}")
def getProductId(id: str):
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.consultaId(id)  # Consultar film por ID
    return data

# Ruta para crear un nuevo film
@app.post("/film/")
def createFilm(film: Film):
    data = filmDB.createFilm(film)  # Crear nuevo film en la base de datos
    return data

# Ruta para actualizar un film por su ID
@app.put("/film/{id}")
def updateProduct(id: str, film: Film):
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.updateFilms(id, film)  # Actualizar film en la base de datos
    return data

# Ruta para eliminar un film por su ID
@app.delete("/film/{id}")
def deleteProduct(id: str):
    clientPM.dbFilms()  # Conectar a la base de datos
    data = filmDB.deleteFilm(id)  # Eliminar film de la base de datos
    return data
