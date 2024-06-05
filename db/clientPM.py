import pymongo

#Hacer conexión de la BD
def dbFilms():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/").M07 #M07 nombre BD de mongo
    except Exception as e:
        print(f"ERROR: {e}")