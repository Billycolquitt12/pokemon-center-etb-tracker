USE pokemon_item_tracker;

-- Force user_id = 1 to exist
INSERT INTO Users (user_id, username, email)
VALUES (1, 'sealedcollector', 'sealed@email.com')
ON DUPLICATE KEY UPDATE
username = VALUES(username),
email = VALUES(email);

-- Force set_id 1-4
INSERT INTO ProductSets (set_id, set_name, release_year) VALUES
(1, 'Crown Zenith', 2023),
(2, 'Paldean Fates', 2024),
(3, 'Stellar Crown', 2024),
(4, 'Twilight Masquerade', 2024)
ON DUPLICATE KEY UPDATE
set_name = VALUES(set_name),
release_year = VALUES(release_year);

-- Force item_id 1-4 (these depend on user_id=1 and set_id=1..4)
INSERT INTO PokemonItems (item_id, user_id, set_id, item_name, sealed) VALUES
(1, 1, 1, 'Pokemon Center Crown Zenith ETB', TRUE),
(2, 1, 2, 'Pokemon Center Paldean Fates ETB', TRUE),
(3, 1, 3, 'Pokemon Center Stellar Crown ETB', TRUE),
(4, 1, 4, 'Pokemon Center Twilight Masquerade ETB', TRUE)
ON DUPLICATE KEY UPDATE
user_id = VALUES(user_id),
set_id = VALUES(set_id),
item_name = VALUES(item_name),
sealed = VALUES(sealed);

-- Prevent duplicate history if rerun
DELETE FROM ItemValues WHERE item_id IN (1,2,3,4);

INSERT INTO ItemValues (item_id, market_value, recorded_date) VALUES
(1, 142.00, '2025-01-01'),
(1, 145.00, '2025-02-01'),
(1, 148.00, '2025-03-01'),
(1, 150.00, '2025-04-01'),
(1, 152.00, '2025-05-01'),
(1, 155.00, '2025-06-01'),
(1, 158.00, '2025-07-01'),
(1, 160.00, '2025-08-01'),

(2, 87.00, '2025-01-01'),
(2, 89.00, '2025-02-01'),
(2, 91.00, '2025-03-01'),
(2, 93.00, '2025-04-01'),
(2, 95.00, '2025-05-01'),
(2, 97.00, '2025-06-01'),
(2, 99.00, '2025-07-01'),
(2, 101.00, '2025-08-01'),

(3, 80.00, '2025-01-01'),
(3, 82.00, '2025-02-01'),
(3, 84.00, '2025-03-01'),
(3, 86.00, '2025-04-01'),
(3, 88.00, '2025-05-01'),
(3, 90.00, '2025-06-01'),
(3, 92.00, '2025-07-01'),
(3, 94.00, '2025-08-01'),

(4, 76.00, '2025-01-01'),
(4, 78.00, '2025-02-01'),
(4, 80.00, '2025-03-01'),
(4, 82.00, '2025-04-01'),
(4, 84.00, '2025-05-01'),
(4, 86.00, '2025-06-01'),
(4, 88.00, '2025-07-01'),
(4, 90.00, '2025-08-01');

-- Sanity check (run these and confirm you see rows)
SELECT * FROM Users;
SELECT * FROM ProductSets;
SELECT * FROM PokemonItems;

USE pokemon_item_tracker;

SELECT item_id, user_id, set_id, item_name, sealed
FROM PokemonItems
ORDER BY item_id DESC
LIMIT 10;