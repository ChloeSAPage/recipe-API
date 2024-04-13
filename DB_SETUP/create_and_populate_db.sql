CREATE DATABASE Cookbook;
USE Cookbook;

CREATE TABLE recipes (
	recipe_id INTEGER AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL UNIQUE,
    instructions VARCHAR(500),
	CONSTRAINT PK_recipe PRIMARY KEY(recipe_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE ingredients (
	ingredient_id INTEGER AUTO_INCREMENT,
    recipe_id INTEGER,
    ingredient VARCHAR(100),
    measurement INTEGER,
    unit VARCHAR(10),
    CONSTRAINT PK_ingredients PRIMARY KEY(ingredient_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE ingredients
ADD CONSTRAINT
FK_recipe_id
FOREIGN KEY(recipe_id)
REFERENCES recipes(recipe_id);

INSERT INTO recipes
(title, instructions)
VALUES
("Beans On Toast", "1: Cook the beans following package instructions,
2: Toast the Bread,
3: Butter the bread,
4: Put Beans on Bread,
5: Enjoy!"),
("Cereal", "You know how to make cereal");

INSERT INTO ingredients
(recipe_id, ingredient, measurement, unit)
VALUES
(1, "Beans", 1, "Tin"),
(1, "Butter", 1, "Spread"),
(1, "Bread", 2, "Slices"),
(2, "Cereal", 1, "Pour"),
(2, "Milk", 1, "Splash"),
(2, "Bowl", 1, "Bowl");

INSERT INTO recipes
(title, instructions)
VALUES
("Beans On Toast", "1: Cook the beans following package instructions,
2: Toast the Bread,
3: Butter the bread,
4: Put Beans on Bread,
5: Enjoy!"),
("Cereal", "You know how to make cereal");