CREATE TABLE Recipes (
    id INT PRIMARY KEY IDENTITY(1,1),
    [name] VARCHAR(100) NOT NULL,
    instructions TEXT,
    total_cooking_time INT
);

CREATE TABLE Ingredients (
    id INT PRIMARY KEY IDENTITY(1,1),
    [name] VARCHAR(100) NOT NULL,
    alternatives VARCHAR(100)
);

CREATE TABLE Hardware (
    id INT PRIMARY KEY IDENTITY(1,1),
    [name] VARCHAR(100)
);

CREATE TABLE Categories (
    id INT PRIMARY KEY IDENTITY(1,1),
    [name] VARCHAR(100)
);

CREATE TABLE RecipeIngredients (
    recipe_id INT FOREIGN KEY REFERENCES Recipes(id),
    ingredient_id INT FOREIGN KEY REFERENCES Ingredients(id),
    quantity VARCHAR(50)
);

CREATE TABLE RecipeHardware (
    recipe_id INT FOREIGN KEY REFERENCES Recipes(id),
    hardware_id INT FOREIGN KEY REFERENCES Hardware(id)
);

CREATE TABLE RecipeCategories (
    recipe_id INT FOREIGN KEY REFERENCES Recipes(id),
    category_id INT FOREIGN KEY REFERENCES Categories(id)
);