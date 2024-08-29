-- The Recipes table stores information about each recipe.
CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    "name" TEXT NOT NULL,
    instructions TEXT,
    total_cooking_time INT
);

-- The Ingredients table stores information about each ingredient that can be used in recipes.
CREATE TABLE Ingredients (
    id SERIAL PRIMARY KEY,
    "name" TEXT NOT NULL,
    alternatives TEXT
);

-- The Hardware table stores information about each piece of hardware that can be used in recipes.
CREATE TABLE Hardware (
    id SERIAL PRIMARY KEY,
    "name" TEXT
);

-- The Categories table stores different categories that a recipe can belong to.
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    "name" TEXT
);

-- The RecipeIngredients table links recipes and ingredients together.
CREATE TABLE RecipeIngredients (
    recipe_id INT REFERENCES Recipes(id),
    ingredient_id INT REFERENCES Ingredients(id),
    quantity TEXT
);

-- The RecipeHardware table links recipes and hardware together.
CREATE TABLE RecipeHardware (
    recipe_id INT REFERENCES Recipes(id),
    hardware_id INT REFERENCES Hardware(id)
);

-- The RecipeCategories table links recipes and categories together.
CREATE TABLE RecipeCategories (
    recipe_id INT REFERENCES Recipes(id),
    category_id INT REFERENCES Categories(id)
);