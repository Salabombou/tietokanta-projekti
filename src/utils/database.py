import os
from psycopg2.extensions import cursor

from typing import Dict


def search_recipe_name(cursor: cursor):
    os.system("clear")
    print("Search Recipes by Name\n")

    search = input("Search: ")

    cursor.execute("SELECT * FROM Recipes WHERE \"name\" LIKE %s", (f"%{search}%",))
    recipes = cursor.fetchall()

    return recipes


def search_recipe_ingredients(cursor: cursor):
    os.system("clear")
    print("Search Recipes by Ingredients\n")

    search = input("Search: ")

    cursor.execute(
        "SELECT * FROM Recipes WHERE \"name\" IN (SELECT \"name\" FROM Ingredients WHERE \"name\" LIKE %s)",
        (f"%{search}%",),
    )
    recipes = cursor.fetchall()

    return recipes


def search_recipe(cursor: cursor):
    os.system("clear")
    print("Search Recipe\n")

    print("Search by: ")

    print("1: Name")
    print("2: Ingredients")
    print("q: Main Menu")

    results = []
    match (input()):
        case "1":
            results = search_recipe_name(cursor)
        case "2":
            results = search_recipe_ingredients(cursor)
        case "q":
            return
        case _:
            search_recipe(cursor)
            return

    os.system("clear")

    for recipe in results:
        print(f"{recipe[1]}: {recipe[2]}")

    print("\nPress any key to continue...")
    input()


def view_recipe(cursor: cursor):
    recipes = search_recipe_name(cursor)
    os.system("clear")
    if len(recipes) == 0:
        print("No recipes found!")
        print("\nPress any key to continue...")
        input()
        return

    print("View Recipe\n")

    print("Select a recipe to view: ")

    for i, recipe in enumerate(recipes):
        print(f"{i + 1}: {recipe[1]}")
    print("q: Main Menu")

    key = ""
    while True:
        key = input()
        if key == "q":
            return
        elif key.isdigit() and 0 < int(key) <= len(recipes):
            break

    recipe = recipes[int(key) - 1]
    recipe_id = recipe[0]
    recipe_name = recipe[1]

    os.system("clear")

    print(f"{recipe_name}\n")

    # Get the ingredients, hardware, and categories
    cursor.execute(
        "SELECT \"name\", quantity FROM Ingredients JOIN RecipeIngredients ON Ingredients.id = RecipeIngredients.ingredient_id WHERE recipe_id = %s",
        (recipe_id,),
    )
    ingredients = cursor.fetchall()

    cursor.execute(
        "SELECT \"name\" FROM Hardware JOIN RecipeHardware ON Hardware.id = RecipeHardware.hardware_id WHERE recipe_id = %s",
        (recipe_id,),
    )
    hardware = cursor.fetchall()

    cursor.execute(
        "SELECT \"name\" FROM Categories JOIN RecipeCategories ON Categories.id = RecipeCategories.category_id WHERE recipe_id = %s",
        (recipe_id,),
    )
    categories = cursor.fetchall()
    
    # Get all recipe names with similar categories
    cursor.execute(
        "SELECT \"name\" FROM Recipes WHERE id IN (SELECT recipe_id FROM RecipeCategories WHERE category_id IN (SELECT category_id FROM RecipeCategories WHERE recipe_id = %s)) AND id != %s",
        (recipe_id, recipe_id),
    )
    similar_recipes = cursor.fetchall()

    print("Ingredients:")
    for ingredient in ingredients:
        print(f"{ingredient[0]}: {ingredient[1]}")
    print()

    print("Hardware:")
    print(", ".join((h[0] for h in hardware)) + "\n")

    print("Categories:")
    print(", ".join((c[0] for c in categories)) + "\n")

    print("Instructions:")
    print(recipe[2] + "\n")

    print("Total cooking time:")
    print(f"{recipe[3]} minutes\n")
    
    print("You might also like:")
    print(", ".join((r[0] for r in similar_recipes)) + "\n")
    

    print("\nPress any key to continue...")
    input()


def add_recipe(cursor: cursor):
    quantity: Dict[str, str] = {}

    os.system("clear")
    print("Add Recipe\n")

    name = input("Name: ")

    ingredients = (i.strip() for i in input("Ingredients: ").split(","))
    for ingredient in ingredients:
        quantity[ingredient] = input(f"Amount of {ingredient}: ")

        alternatives = ",".join(
            [
                a.strip()
                for a in input(f"Possible alternatives for {ingredient}: ").split(",")
            ]
        )

        # Check if ingredient is in the database
        cursor.execute("SELECT * FROM Ingredients WHERE \"name\" = %s", (ingredient,))
        result = cursor.fetchone()
        if result is None:
            # Ingredient is not in the database, so add it
            cursor.execute(
                "INSERT INTO Ingredients (\"name\", alternatives) VALUES (%s, %s)",
                (ingredient, alternatives),
            )
        elif len(alternatives) > 0:
            # Update the alternatives

            # Get the current alternatives
            cursor.execute(
                "SELECT alternatives FROM Ingredients WHERE \"name\" = %s", (ingredient,)
            )
            current_alternatives = (cursor.fetchone() or [""])[0].split(",")

            # Combine the current alternatives with the new ones
            alternatives = ",".join(set(current_alternatives + alternatives.split(",")))

            # Update the alternatives
            cursor.execute(
                "UPDATE Ingredients SET alternatives = %s WHERE \"name\" = %s",
                (alternatives, ingredient),
            )

    hardware = (h.strip() for h in input("Hardware: ").split(","))
    for hardware in hardware:
        # Check if hardware is in the database
        cursor.execute("SELECT * FROM Hardware WHERE \"name\" = %s", (hardware,))
        result = cursor.fetchone()
        if result is None:
            # Hardware is not in the database, so add it
            cursor.execute("INSERT INTO Hardware (\"name\") VALUES (%s)", (hardware,))

    categories = (c.strip() for c in input("Categories: ").split(","))
    for category in categories:
        # Check if category is in the database
        cursor.execute("SELECT * FROM Categories WHERE \"name\" = %s", (category,))
        result = cursor.fetchone()
        if result is None:
            # Category is not in the database, so add it
            cursor.execute("INSERT INTO Categories (\"name\") VALUES (%s)", (category,))

    instructions = input("Instructions: ")

    total_cooking_time = input("Total cooking time (minutes): ")

    # Add the recipe
    cursor.execute(
        "INSERT INTO Recipes (\"name\", instructions, total_cooking_time) VALUES (%s, %s, %s)",
        (name, instructions, total_cooking_time),
    )

    cursor.execute("SELECT SCOPE_IDENTITY()")
    recipe_id = cursor.fetchone()[0]

    for ingredient in ingredients:
        cursor.execute("SELECT id FROM Ingredients WHERE \"name\" = %s", (ingredient,))
        ingredient_id = cursor.fetchone()
        if ingredient_id is None:
            cursor.execute(
                "INSERT INTO Ingredients (\"name\") VALUES (%s)", (ingredient,)
            )
            cursor.execute("SELECT SCOPE_IDENTITY()")
            ingredient_id = cursor.fetchone()
        ingredient_id = ingredient_id[0]

        cursor.execute(
            "INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)",
            (recipe_id, ingredient_id, quantity[ingredient]),
        )

    for hardware in hardware:
        cursor.execute("SELECT id FROM Hardware WHERE \"name\" = %s", (hardware,))
        hardware_id = cursor.fetchone()
        if hardware_id is None:
            cursor.execute("INSERT INTO Hardware (\"name\") VALUES (%s)", (hardware,))
            cursor.execute("SELECT SCOPE_IDENTITY()")
            hardware_id = cursor.fetchone()
        hardware_id = hardware_id[0]

        cursor.execute(
            "INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES (%s, %s)",
            (recipe_id, hardware_id),
        )

    for category in categories:
        cursor.execute("SELECT id FROM Categories WHERE \"name\" = %s", (category,))
        category_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO RecipeCategories (recipe_id, category_id) VALUES (%s, %s)",
            (recipe_id, category_id),
        )

    print("Recipe added!")
    print("\nPress any key to continue...")
    input()


def update_recipe(cursor: cursor):
    recipes = search_recipe_name(cursor)
    if len(recipes) == 0:
        print("No recipes found!")
        print("\nPress any key to continue...")
        input()
        return

    os.system("clear")

    print("Update Recipe\n")

    print("Select a recipe to update: ")

    for i, recipe in enumerate(recipes):
        print(f"{i + 1}: {recipe[1]}")

    print("q: Main Menu")

    key = ""
    while True:
        key = input()
        if key == "q":
            return
        elif key.isdigit() and 0 < int(key) <= len(recipes):
            break

    recipe = recipes[int(key) - 1]
    recipe_id = recipe[0]

    os.system("clear")

    print(f"Update Recipe ({recipe[1]})\n")

    if input("Update name? (y/n): ").lower() == "y":
        name = input(f"Name: ")
        cursor.execute(
            "UPDATE Recipes SET \"name\" = %s WHERE id = %s", (name, recipe_id)
        )

    if input("Update ingredients? (y/n): ").lower() == "y":
        quantity: Dict[str, str] = {}
        ingredients = (i.strip() for i in input(f"Ingredients: ").split(","))
        for ingredient in ingredients:
            quantity[ingredient] = input(f"Amount of {ingredient}: ")

            alternatives = ",".join(
                [
                    a.strip()
                    for a in input(f"Possible alternatives for {ingredient}: ").split(
                        ","
                    )
                ]
            )

            # Check if ingredient is in the database
            cursor.execute("SELECT * FROM Ingredients WHERE \"name\" = %s", (ingredient,))
            result = cursor.fetchone()
            if result is None:
                # Ingredient is not in the database, so add it
                cursor.execute(
                    "INSERT INTO Ingredients (\"name\", alternatives) VALUES (%s, %s)",
                    (ingredient, alternatives),
                )
            elif len(alternatives) > 0:
                # Update the alternatives

                # Get the current alternatives
                cursor.execute(
                    "SELECT alternatives FROM Ingredients WHERE \"name\" = %s",
                    (ingredient,),
                )
                current_alternatives = (cursor.fetchone() or [""])[0].split(",")

                # Combine the current alternatives with the new ones
                alternatives = ",".join(
                    set(current_alternatives + alternatives.split(","))
                )

                # Update the alternatives
                cursor.execute(
                    "UPDATE Ingredients SET alternatives = %s WHERE \"name\" = %s",
                    (alternatives, ingredient),
                )

        cursor.execute(
            "DELETE FROM RecipeIngredients WHERE recipe_id = %s", (recipe_id,)
        )
        for ingredient in ingredients:
            cursor.execute(
                "SELECT id FROM Ingredients WHERE \"name\" = %s", (ingredient,)
            )
            ingredient_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)",
                (recipe_id, ingredient_id, quantity[ingredient]),
            )

    if input("Update hardware? (y/n): ").lower() == "y":
        hardware = (h.strip() for h in input(f"Hardware: ").split(","))
        cursor.execute("DELETE FROM RecipeHardware WHERE recipe_id = %s", (recipe_id,))
        for hardware in hardware:
            # Check if hardware is in the database
            cursor.execute("SELECT * FROM Hardware WHERE \"name\" = %s", (hardware,))
            result = cursor.fetchone()
            if result is None:
                # Hardware is not in the database, so add it
                cursor.execute("INSERT INTO Hardware (\"name\") VALUES (%s)", (hardware,))

            cursor.execute("SELECT id FROM Hardware WHERE \"name\" = %s", (hardware,))
            hardware_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES (%s, %s)",
                (recipe_id, hardware_id),
            )

    if input("Update categories? (y/n): ").lower() == "y":
        categories = (c.strip() for c in input(f"Categories: ").split(","))
        cursor.execute(
            "DELETE FROM RecipeCategories WHERE recipe_id = %s", (recipe_id,)
        )
        for category in categories:
            # Check if category is in the database
            cursor.execute("SELECT * FROM Categories WHERE \"name\" = %s", (category,))
            result = cursor.fetchone()
            if result is None:
                # Category is not in the database, so add it
                cursor.execute(
                    "INSERT INTO Categories (\"name\") VALUES (%s)", (category,)
                )

            cursor.execute("SELECT id FROM Categories WHERE \"name\" = %s", (category,))
            category_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO RecipeCategories (recipe_id, category_id) VALUES (%s, %s)",
                (recipe_id, category_id),
            )

    if input("Update instructions? (y/n): ").lower() == "y":
        instructions = input(f"Instructions: ")
        cursor.execute(
            "UPDATE Recipes SET instructions = %s WHERE id = %s",
            (instructions, recipe_id),
        )

    if input("Update total cooking time? (y/n): ").lower() == "y":
        total_cooking_time = input(f"Total cooking time (minutes): ")
        cursor.execute(
            "UPDATE Recipes SET total_cooking_time = %s WHERE id = %s",
            (total_cooking_time, recipe_id),
        )

    print("Recipe updated!")
    print("\nPress any key to continue...")
    input()


def delete_recipe(cursor: cursor):
    recipes = search_recipe_name(cursor)
    if len(recipes) == 0:
        print("No recipes found!")
        print("\nPress any key to continue...")
        input()
        return

    os.system("clear")

    print("Delete Recipe\n")

    print("Select a recipe to delete: ")

    for i, recipe in enumerate(recipes):
        print(f"{i + 1}: {recipe[1]}")
    print("a: Delete all recipes")
    print("q: Main Menu")

    key = ""
    while True:
        key = input()
        if key == "q":
            return
        elif key == "a":
            if (
                input("Are you sure you want to delete all recipes? (y/n): ").lower()
                == "y"
            ):
                for recipe in recipes:
                    recipe_id = recipe[0]
                    cursor.execute(
                        "DELETE FROM RecipeIngredients WHERE recipe_id = %s",
                        (recipe_id),
                    )
                    cursor.execute(
                        "DELETE FROM RecipeHardware WHERE recipe_id = %s", (recipe_id)
                    )
                    cursor.execute(
                        "DELETE FROM RecipeCategories WHERE recipe_id = %s", (recipe_id)
                    )
                    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id))
                print("All recipes deleted!")
            else:
                print("Recipes not deleted!")

            print("\nPress any key to continue...")
            input()
            return
        elif key.isdigit() and 0 < int(key) <= len(recipes):
            break

    recipe = recipes[int(key) - 1]
    recipe_id = recipe[0]

    os.system("clear")
    
    print(f"Delete Recipe ({recipe[1]})\n")

    if input("Are you sure you want to delete this recipe? (y/n): ").lower() == "y":
        cursor.execute(
            "DELETE FROM RecipeIngredients WHERE recipe_id = %s", (recipe_id,)
        )
        cursor.execute("DELETE FROM RecipeHardware WHERE recipe_id = %s", (recipe_id,))
        cursor.execute("DELETE FROM RecipeCategories WHERE recipe_id = %s", (recipe_id,))
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))

        print("Recipe deleted!")
    else:
        print("Recipe not deleted!")

    print("\nPress any key to continue...")
    input()
