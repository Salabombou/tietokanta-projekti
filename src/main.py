import pymssql
import os

from utils import database


def mainmenu(cursor: pymssql.Cursor):
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
    conn = pymssql.connect(
        server="mssql",
        user="sa",
        password="Nakkikastike12",
        database="RecipeDB",
    )
    cursor = conn.cursor()

    try:
        mainmenu(cursor)
    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()  # print a newline after the ^C
