import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dados_local"]

carros_collection = db["Carros"]
montadoras_collection = db["Montadoras"]

montadoras_data = [
    {"Montadora": "Chevrolet", "Pais": "EUA"},
    {"Montadora": "Volkswagen", "Pais": "Alemanha"},
    {"Montadora": "Renaut", "Pais": "Franca"},
    {"Montadora": "Ford", "Pais": "EUA"},
    {"Montadora": "Honda", "Pais": "Japao"},
]

carros_data = [
    {"Carro": "Onix", "Cor": "Prata", "Montadora": "Chevrolet"},
    {"Carro": "Polo", "Cor": "Branco", "Montadora": "Volkswagen"},
    {"Carro": "Sandero", "Cor": "Prata", "Montadora": "Renaut"},
    {"Carro": "Fiesta", "Cor": "Vermelho", "Montadora": "Ford"},
    {"Carro": "City", "Cor": "Preto", "Montadora": "Honda"},
]

montadoras_collection.insert_many(montadoras_data)
carros_collection.insert_many(carros_data)

client.close()