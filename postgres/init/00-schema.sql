CREATE TABLE Recipes (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    instructions TEXT,
    total_cooking_time INT
);

CREATE TABLE Ingredients (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    alternatives VARCHAR(100)
);

CREATE TABLE Hardware (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(100)
);

CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(100)
);

CREATE TABLE RecipeIngredients (
    recipe_id INT REFERENCES Recipes(id),
    ingredient_id INT REFERENCES Ingredients(id),
    quantity VARCHAR(50)
);

CREATE TABLE RecipeHardware (
    recipe_id INT REFERENCES Recipes(id),
    hardware_id INT REFERENCES Hardware(id)
);

CREATE TABLE RecipeCategories (
    recipe_id INT REFERENCES Recipes(id),
    category_id INT REFERENCES Categories(id)
);