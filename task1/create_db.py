from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://erterujamp:RB7ydmry8ldG0rV9@erter.krt7i.mongodb.net/?retryWrites=true&w=majority&appName=ERTER",
    server_api=ServerApi("1"),
)

dataBase = client.my_new_cats

dataBase.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)
