
-- Search recipes by name
SELECT * FROM Recipes WHERE "name" LIKE %<search>%

-- Get all ingredients by name
SELECT * FROM Ingredients WHERE "name" = <ingredient_name>

-- Get all hardware by name
SELECT * FROM Hardware WHERE "name" = <hardware_name>

-- Get all categories by name
SELECT * FROM Categories WHERE "name" = <category_name>


-- Get all recipes with a specific ingredient
SELECT * FROM Recipes WHERE "name" IN (
    SELECT "name" FROM Ingredients WHERE "name" LIKE %<ingredient_name>%
)

-- Get all alternative ingredients for a specific ingredient
SELECT alternatives FROM Ingredients WHERE "name" = <ingredient_name>



-- Get ingredient id
SELECT id FROM Ingredients WHERE "name" = <ingredient_name>

-- Get hardware id
SELECT id FROM Categories WHERE "name" = <category_name>

-- Get category id
SELECT id FROM Hardware WHERE "name" = <hardware_name>



-- Get all ingredients with their quantities for a recipe
SELECT "name", quantity FROM Ingredients JOIN RecipeIngredients ON Ingredients.id = RecipeIngredients.ingredient_id WHERE recipe_id = <recipe_id>

-- Get all hardware for a recipe
SELECT "name" FROM Hardware JOIN RecipeHardware ON Hardware.id = RecipeHardware.hardware_id WHERE recipe_id = <recipe_id>

-- Get all categories for a recipe
SELECT "name" FROM Categories JOIN RecipeCategories ON Categories.id = RecipeCategories.category_id WHERE recipe_id = <recipe_id>

-- Get similar recipes based on categories
SELECT "name" FROM Recipes WHERE id IN (
    SELECT recipe_id FROM RecipeCategories WHERE category_id IN (
        SELECT category_id FROM RecipeCategories WHERE recipe_id = <recipe_id>
    )
) AND id != <recipe_id>


-- Add a new recipe
INSERT INTO Recipes ("name", instructions, total_cooking_time) VALUES (<recipe_name>, <instructions>, <cooking_time>)

-- Add the ingredients of a recipe
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (<recipe_id>, <ingredient_id>, <quantity>)

-- Add the hardware of a recipe
INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES (<recipe_id>, <hardware_id>)

-- Add the categories of a recipe
INSERT INTO RecipeCategories (recipe_id, category_id) VALUES (<recipe_id>, <category_id>)

-- Add a new ingredient
INSERT INTO Ingredients ("name") VALUES (<ingredient_name>)

-- Add a new ingredient with alternatives
INSERT INTO Ingredients ("name", alternatives) VALUES (<ingredient_name>, <alternatives>)

-- Add a new hardware
INSERT INTO Hardware ("name") VALUES (<hardware_name>)

-- Add a new category
INSERT INTO Categories ("name") VALUES (<category_name>)


-- Update recipe name
UPDATE Recipes SET "name" = <recipe_name> WHERE id = <recipe_id>

-- Update recipe cooking time
UPDATE Recipes SET total_cooking_time = <cooking_time> WHERE id = <recipe_id>

-- Update recipe instructions
UPDATE Recipes SET instructions = <instructions> WHERE id = <recipe_id>

-- Update ingredient alternatives
UPDATE Ingredients SET alternatives = <alternatives> WHERE "name" = <ingredient_name>



-- Delete a recipe
DELETE FROM Recipes WHERE id = <recipe_id>

-- Delete recipe ingredients
DELETE FROM RecipeIngredients WHERE recipe_id = <recipe_id>

-- Delete recipe hardware
DELETE FROM RecipeHardware WHERE recipe_id = <recipe_id>

-- Delete recipe categories
DELETE FROM RecipeCategories WHERE recipe_id = <recipe_id>
