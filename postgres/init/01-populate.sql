-- Inserting some ingredients
INSERT INTO Ingredients ("name", alternatives) VALUES 
('Flour', 'Almond flour'),
('Sugar', 'Honey'),
('Eggs', 'Banana'),
('Milk', 'Almond milk');

-- Inserting some hardware
INSERT INTO Hardware ("name") VALUES 
('Oven'),
('Mixing bowl'),
('Whisk'),
('Baking tray');

-- Inserting some categories
INSERT INTO Categories ("name") VALUES 
('Dessert'),
('Main Course'),
('Appetizer');

-- Inserting some recipes
INSERT INTO Recipes ("name", instructions, total_cooking_time) VALUES 
('Blueberry Pie', 'Mix ingredients and bake in oven for 45 minutes.', 45),
('Raspberry Pie', 'Mix ingredients and bake in oven for 40 minutes.', 40);

-- Linking recipes and ingredients
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES 
(1, 1, '2 cups'),
(1, 2, '1 cup'),
(1, 3, '2'),
(1, 4, '1 cup'),
(2, 1, '2 cups'),
(2, 2, '1 cup'),
(2, 3, '2'),
(2, 4, '1 cup');

-- Linking recipes and hardware
INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4);

-- Linking recipes and categories
INSERT INTO RecipeCategories (recipe_id, category_id) VALUES 
(1, 1),
(2, 1);