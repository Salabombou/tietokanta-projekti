import psycopg2
import os

from utils import database


def mainmenu(cursor):
    """
    This function displays the main menu of the application and handles user input.
    It calls the appropriate database function based on the user's choice.

    Args:
        cursor (psycopg2.extensions.cursor): The cursor to interact with the PostgreSQL database.
    """
    print("1: View Recipe")
    print("2: Add Recipe")
    print("3: Update Recipe")
    print("4: Delete Recipe")
    print("q: Quit")

    match (input()):
        case "1":
            database.view_recipe(cursor)
        case "2":
            database.add_recipe(cursor)
        case "3":
            database.update_recipe(cursor)
        case "4":
            database.delete_recipe(cursor)
        case "q":
            return
    mainmenu(cursor)


def mainmenu(cursor: psycopg2.extensions.cursor):
    os.system("clear")
    print("Tietokanta Projekti\n")
    print("Options\n")

    print("1: View Recipe")
    print("2: Add Recipe")
    print("3: Update Recipe")
    print("4: Delete Recipe")
    print("q: Quit")

    match (input()):
        case "1":
            database.view_recipe(cursor)
        case "2":
            database.add_recipe(cursor)
        case "3":
            database.update_recipe(cursor)
        case "4":
            database.delete_recipe(cursor)
        case "q":
            return
    mainmenu(cursor)


def main():
    connection = psycopg2.connect(
        user="admin",
        password="Nakkikastike12",
        host="postgres",
        port="5432",
        database="RecipeDB"
    )
    
    try:
        cursor = connection.cursor()
        mainmenu(cursor)
    finally:
        connection.commit()
        connection.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()  # print a newline after the ^C
