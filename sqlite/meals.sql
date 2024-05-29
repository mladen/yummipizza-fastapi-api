-- create_meals.sql

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS meals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  price INTEGER NOT NULL,
  path_to_photo TEXT NOT NULL
);

INSERT INTO meals (id, name, description, price, path_to_photo) VALUES
(1, 'Black Olives Pizza', 'Mediterranean style pizza with black olives', 4, 'blackolives.jpeg'),
(2, 'Bianca', 'Pizza with eggs', 7, 'eggs.jpeg'),
(3, 'Pepperoni pizza', 'Yummy pepperoni pizza', 8, 'pepperoni.jpeg'),
(4, 'Sausage', 'Sausage pizza', 7, 'sausage.jpeg'),
(5, 'Tomato + Olives', 'Vegetarian pizza', 6, 'tomatoolives.jpeg'),
(6, 'Pancakes with jam', 'Yummi pancakes', 3, 'pancakesjam.jpg');

COMMIT;
