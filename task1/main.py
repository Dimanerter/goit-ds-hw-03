from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os


# Перевіряє, чи є ім'я в базі перед виконанням функції
def checkname(func):
    def wrapper(dataBase, name):
        if dataBase.cats.find_one({"name": name}) is None:
            print("Не знайдено")  # Якщо імені немає
        else:
            func(dataBase, name)  # Викликає функцію, якщо ім'я знайдено

    return wrapper


# Розбиває введення користувача на команду та аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()  # Розділяє введення
    cmd = cmd.strip().lower()  # Зводить команду до нижнього регістру
    return cmd, *args


# Виводить усі документи в колекції 'cats'
def show_all(dataBase):
    result = dataBase.cats.find({})  # Знаходить усі документи
    if result is None:
        print("Не знайдено")
    else:
        for i in result:
            print(i)  # Виводить документи


# Виводить документ за ім'ям
def show_by_name(dataBase, name):
    result = dataBase.cats.find_one({"name": name})
    if result is None:
        print("Не знайдено")
    else:
        print(result)


# Оновлює вік за ім'ям (з перевіркою наявності імені)
@checkname
def update_age_by_name(dataBase, name):
    new_age = int(input("Вкажіть новий вік: "))  # Запитує новий вік
    dataBase.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Оновлено")


# Додає нову властивість до 'features' за ім'ям (з перевіркою наявності)
@checkname
def add_features_by_name(dataBase, name):
    new_feature = input("Вкажіть нову властивість: ")  # Запитує нову властивість
    dataBase.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
    print("Оновлено")


# Видаляє документ за ім'ям
def delete_by_name(dataBase, name):
    dataBase.cats.delete_one({"name": name})  # Видаляє документ
    print("Видалено")


# Видаляє всі документи в колекції
def delete_all(dataBase):
    dataBase.cats.delete_many({})  # Видаляє всі документи
    print("Видалено")


client = MongoClient(
    "mongodb+srv://erterujamp:RB7ydmry8ldG0rV9@erter.krt7i.mongodb.net/?retryWrites=true&w=majority&appName=ERTER",
    server_api=ServerApi("1"),
)

dataBase = client.my_new_cats

if __name__ == "__main__":
    os.system("clear")
    while True:
        print(
            """You have 7 options: 
                all            - to show all cats
                output "name"  - to show cat by name
                update ""name  - to update age by name
                add "name"     - to add features by name
                delete "name"  - to delete by name
                delete all     - to delete all
                exit           - to exit"""
        )
        chois = input("Please write your choice: ")
        os.system("clear")
        command, *args = parse_input(chois)
        try:
            match command:
                case "all":
                    show_all(dataBase)
                case "output":
                    show_by_name(dataBase, *args)
                case "update":
                    update_age_by_name(dataBase, *args)
                case "add":
                    add_features_by_name(dataBase, *args)
                case "delete":
                    delete_by_name(dataBase, *args)
                case "delete all":
                    delete_all(dataBase)
                case "exit":
                    break
                case _:
                    print("Invalid command")
        except Exception:
            print("Error")
        print("\n\n")
