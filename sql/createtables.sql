DROP DATABASE IF EXISTS pokemon_item_tracker;
CREATE DATABASE pokemon_item_tracker;
USE pokemon_item_tracker;

-- USERS
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- PRODUCT SETS
CREATE TABLE ProductSets (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    set_name VARCHAR(100) NOT NULL,
    release_year INT
);

-- ITEMS
CREATE TABLE PokemonItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    set_id INT NOT NULL,
    item_name VARCHAR(150) NOT NULL,
    sealed BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT fk_items_user
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_items_set
        FOREIGN KEY (set_id) REFERENCES ProductSets(set_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- PRICE HISTORY
CREATE TABLE ItemValues (
    value_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    market_value DECIMAL(8,2) NOT NULL,
    recorded_date DATE NOT NULL,

    CONSTRAINT fk_values_item
        FOREIGN KEY (item_id) REFERENCES PokemonItems(item_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


