from pymongo import MongoClient
from pymongo.server_api import ServerApi


def show_all(dataBase):
    result = dataBase.cats.find({})
    for i in result:
        print(i)


def show_by_name(dataBase, name):
    result = dataBase.cats.find_one({"name": name})
    if result is None:
        print("Not found")
    else:
        print(result)


client = MongoClient(
    "mongodb+srv://erterujamp:RB7ydmry8ldG0rV9@erter.krt7i.mongodb.net/?retryWrites=true&w=majority&appName=ERTER",
    server_api=ServerApi("1"),
)

dataBase = client.my_new_cats

if __name__ == "__main__":
    while True:
        chois = input("Please write 'all' or cat's name to show all cats or by name: ")
        try:
            match chois:
                case "all":
                    show_all(dataBase)
                case "exit":
                    break
                case _:
                    show_by_name(dataBase, chois)
        except Exception:
            print("Error")
