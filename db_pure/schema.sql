CREATE TABLE dish (
    id SERIAL PRIMARY KEY,
    name TEXT,
    photo_url TEXT,
    description TEXT,
    cooking_time SMALLINT
);

CREATE TABLE ingredient (
    id SERIAL PRIMARY KEY,
    name TEXT,
    photo_url TEXT,
    category TEXT,
    description TEXT,
    calories FLOAT,
    proteins FLOAT,
    fats FLOAT,
    carbs FLOAT,
    price FLOAT
);

CREATE TABLE dish_ingredient_link (
    dish_id INTEGER REFERENCES dish(id),
    ingredient_id INTEGER REFERENCES ingredient(id),
    amount SMALLINT,
    pieces SMALLINT
);

CREATE TABLE list_category_dish (
    id SERIAL PRIMARY KEY,
    cat_name TEXT,
    type TEXT
);

CREATE TABLE dish_category_link (
    dish_id INTEGER REFERENCES dish(id),
    type_id INTEGER REFERENCES list_category_dish(id)
);



ALTER TABLE dish
ALTER name SET NOT NULL,
ADD COLUMN slug TEXT NOT NULL DEFAULT ' ';

ALTER TABLE ingredient
ALTER name SET NOT NULL,
ADD COLUMN slug TEXT NOT NULL DEFAULT ' ',
ALTER category SET NOT NULL,
ALTER calories SET DEFAULT 0.0,
ALTER proteins SET DEFAULT 0.0,
ALTER fats SET DEFAULT 0.0,
ALTER carbs SET DEFAULT 0.0,
ALTER price SET NOT NULL;

ALTER TABLE list_category_dish
ALTER cat_name SET NOT NULL,
ALTER type SET NOT NULL;