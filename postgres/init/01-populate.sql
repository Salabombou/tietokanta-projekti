-- Inserting some ingredients
INSERT INTO Ingredients ("name", alternatives) VALUES 
('Flour', 'Almond flour'),
('Sugar', 'Honey'),
('Eggs', 'Banana'),
('Milk', 'Almond milk'),
('Macaroni', 'Any Short Pasta'),
('Minced meat', 'Vegan minced meat'),
('Egg'),
('Bouillon cube'),
('Water');

-- Inserting some hardware
INSERT INTO Hardware ("name") VALUES 
('Oven'),
('Mixing bowl'),
('Whisk'),
('Baking tray'),
('Frying Pan'),
('Cauldron'),
('Spatula'),
('Ladle'),
('Kettle'),
('Stove');

-- Inserting some categories
INSERT INTO Categories ("name") VALUES 
('Dessert'),
('Main Course'),
('Appetizer');

-- Inserting some recipes
INSERT INTO Recipes ("name", instructions, total_cooking_time) VALUES 
('Blueberry Pie', 'Mix ingredients and bake in oven for 45 minutes.', 45),
('Raspberry Pie', 'Mix ingredients and bake in oven for 40 minutes.', 40),
('Rhubarb Pie', 'Mix ingredients and bake in oven for 30 minutes.', 30),
('Nistipata', 'Fry the meat and cook the macaroni. Mix the meat into the cauldron.', 25),
('Macaroni box', 'Fry the meat and cook the macaroni. Heat water in a kettle and mix it with the eggs and bouillion cubes using a whisk. Stir the mixture. Combine all in the tin. Heat in oven at 175c for 45mins.', 70);

-- Linking recipes and ingredients
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES 
(1, 1, '2 cups'),
(1, 2, '1 cup'),
(1, 3, '2'),
(1, 4, '1 cup'),
(2, 1, '2 cups'),
(2, 2, '1 cup'),
(2, 3, '2'),
(2, 4, '1 cup'),
(3, 1, '2 cups'),
(3, 2, '1 cup'),
(3, 3, '2'),
(3, 4, '1 cup'),
(4, 5, '300g'),
(4, 6, '300g'),
(5, 5, '400g'),
(5, 6, '400g'),
(5, 7, '3'),
(5, 8, '2'),
(5, 9, '1L');
  
-- Linking recipes and hardware
INSERT INTO RecipeHardware (recipe_id, hardware_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(4, 5),
(4, 6),
(4, 10),
(5, 1),
(5, 2),
(5, 3),
(5, 5),
(5, 6),
(5, 7),
(5, 8),
(5, 9),
(5, 10);

-- Linking recipes and categories
INSERT INTO RecipeCategories (recipe_id, category_id) VALUES 
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2);
