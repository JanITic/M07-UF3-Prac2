from db import clientPM
from bson.objectid import ObjectId
from datetime import datetime
import json

# Esquema para convertir un film de la base de datos en un diccionario
def film_schema(film) -> dict:
    return {
        "id": str(film["_id"]),
        "title": film["title"],
        "director": film["director"],
        "year": film["year"],
        "genere": film["genere"],
        "rating": film["rating"],
        "country": film["country"],
    }

# Esquema para convertir una lista de films de la base de datos en una lista de diccionarios
def films_schema(films) -> dict:
    return [film_schema(film) for film in films]

# Función para consultar todos los films
def consulta():
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        data = conn.films.find()  # Obtener todos los films
        result = films_schema(data)  # Convertir los films a diccionarios
        return result
    except Exception as e:
        return f'Error conexión {e}'

# Función para consultar films por género
def consultaGenere(genere):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        data = conn.films.find({"genere": genere})  # Obtener films por género
        result = films_schema(data)  # Convertir los films a diccionarios
        return result
    except Exception as e:
        return f'Error conexión {e}'

# Función para consultar films ordenados por un campo específico
def consultaOrder(field, order):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        data = conn.films.find().sort(field, order)  # Obtener films ordenados
        result = films_schema(data)  # Convertir los films a diccionarios
        return result
    except Exception as e:
        return f'Error conexión {e}'

# Función para consultar un número limitado de films
def consultaLimit(limit):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        data = conn.films.find().limit(limit)  # Obtener films limitados
        result = films_schema(data)  # Convertir los films a diccionarios
        return result
    except Exception as e:
        return f'Error conexión {e}'

# Función para consultar un film por su ID
def consultaId(id):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        data = conn.films.find_one({"_id": ObjectId(id)})  # Obtener film por ID
        result = film_schema(data)  # Convertir el film a diccionario
        return result
    except Exception as e:
        return f'Error conexión {e}'

# Función para crear un nuevo film
def createFilm(film):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        now = datetime.now()  # Fecha y hora actuales
        data = {
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genere": film.genere,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }
        id = conn.films.insert_one(data).inserted_id  # Insertar film en la base de datos
        return {"OK": str(id)}  # Retornar ID del nuevo film
    except Exception as e:
        return f'Error conexión {e}'

# Función para eliminar un film por su ID
def deleteFilm(id):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        conn.films.delete_one({"_id": ObjectId(id)})  # Eliminar film por ID
        return "Film eliminada"
    except Exception as e:
        return f'Error conexión {e}'

# Función para actualizar un film por su ID
def updateFilms(id, film):
    try:
        conn = clientPM.dbFilms()  # Conectar a la base de datos
        now = datetime.now()  # Fecha y hora actuales
        data = {
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genere": film.genere,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }
        conn.films.update_one({"_id": ObjectId(id)}, {"$set": data})  # Actualizar film en la base de datos
        return 'Pelicula actualizada'
    except Exception as e:
        return f'Error conexión {e}'
