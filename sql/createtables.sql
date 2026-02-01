CREATE DATABASE pokemon_item_tracker;
USE pokemon_item_tracker;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE ProductSets (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    set_name VARCHAR(100) NOT NULL,
    release_year INT
);

CREATE TABLE PokemonItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    set_id INT,
    item_name VARCHAR(150) NOT NULL,
    sealed BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (set_id) REFERENCES ProductSets(set_id)
);

CREATE TABLE ItemValues (
    value_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    market_value DECIMAL(8,2),
    recorded_date DATE,
    FOREIGN KEY (item_id) REFERENCES PokemonItems(item_id)
);
