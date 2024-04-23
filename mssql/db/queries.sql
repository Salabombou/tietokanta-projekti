SELECT * FROM Recipes WHERE [name] LIKE %<search>%
SELECT * FROM Ingredients WHERE [name] = <ingredient_name>
SELECT * FROM Hardware WHERE [name] = <hardware_name>
SELECT * FROM Categories WHERE [name] = <category_name>

SELECT * FROM Recipes WHERE [name] IN (SELECT [name] FROM Ingredients WHERE [name] LIKE %<ingredient_name>%)
SELECT alternatives FROM Ingredients WHERE [name] = <ingredient_name>

INSERT INTO Recipes ([name], instructions, total_cooking_time) VALUES (<recipe_name>, <instructions>, <cooking_time>)
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (<recipe_id>, <ingredient_id>, <quantity>)
INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES (<recipe_id>, <hardware_id>)
INSERT INTO RecipeCategories (recipe_id, category_id) VALUES (<recipe_id>, <category_id>)
INSERT INTO Ingredients ([name]) VALUES (<ingredient_name>)
INSERT INTO Ingredients ([name], alternatives) VALUES (<ingredient_name>, <alternatives>)
INSERT INTO Hardware ([name]) VALUES (<hardware_name>)
INSERT INTO Categories ([name]) VALUES (<category_name>)

UPDATE Recipes SET [name] = <recipe_name> WHERE id = <recipe_id>
UPDATE Recipes SET total_cooking_time = <cooking_time> WHERE id = <recipe_id>
UPDATE Recipes SET instructions = <instructions> WHERE id = <recipe_id>
UPDATE Ingredients SET alternatives = <alternatives> WHERE [name] = <ingredient_name>

SELECT id FROM Ingredients WHERE [name] = <ingredient_name>
SELECT id FROM Categories WHERE [name] = <category_name>
SELECT id FROM Hardware WHERE [name] = <hardware_name>

SELECT [name], quantity FROM Ingredients JOIN RecipeIngredients ON Ingredients.id = RecipeIngredients.ingredient_id WHERE recipe_id = <recipe_id>
SELECT [name] FROM Hardware JOIN RecipeHardware ON Hardware.id = RecipeHardware.hardware_id WHERE recipe_id = <recipe_id>
SELECT [name] FROM Categories JOIN RecipeCategories ON Categories.id = RecipeCategories.category_id WHERE recipe_id = <recipe_id>

DELETE FROM Recipes WHERE id = <recipe_id>
DELETE FROM RecipeIngredients WHERE recipe_id = <recipe_id>
DELETE FROM RecipeHardware WHERE recipe_id = <recipe_id>
DELETE FROM RecipeCategories WHERE recipe_id = <recipe_id>
