from pymongo import MongoClient


client = MongoClient()

db = client.get_database("kamino")

aloj = client.kamino.Alojamiento
rest = client.kamino.Restauracion
patr = client.kamino.Patrimonio



































