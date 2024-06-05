from pydantic import BaseModel

# Definición del modelo de datos para un film
class Film(BaseModel):
    title:str
    director:str 
    year:int
    genere:str
    rating:int
    country: str

    