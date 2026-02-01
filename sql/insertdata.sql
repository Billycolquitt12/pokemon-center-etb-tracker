INSERT IGNORE INTO Users (username, email) VALUES
('sealedcollector', 'sealed@email.com');

INSERT IGNORE INTO ProductSets (set_name, release_year) VALUES
('Crown Zenith', 2023),
('Paldean Fates', 2024),
('Stellar Crown', 2024),
('Twilight Masquerade', 2024);

INSERT IGNORE INTO PokemonItems (user_id, set_id, item_name) VALUES
(1, 1, 'Pokemon Center Crown Zenith ETB'),
(1, 2, 'Pokemon Center Paldean Fates ETB'),
(1, 3, 'Pokemon Center Stellar Crown ETB'),
(1, 4, 'Pokemon Center Twilight Masquerade ETB');

INSERT INTO ItemValues (item_id, market_value, recorded_date) VALUES
-- Crown Zenith PC ETB
(1, 142.00, '2025-01-01'),
(1, 145.00, '2025-02-01'),
(1, 148.00, '2025-03-01'),
(1, 150.00, '2025-04-01'),
(1, 152.00, '2025-05-01'),
(1, 155.00, '2025-06-01'),
(1, 158.00, '2025-07-01'),
(1, 160.00, '2025-08-01'),

-- Paldean Fates PC ETB
(2, 87.00, '2025-01-01'),
(2, 89.00, '2025-02-01'),
(2, 91.00, '2025-03-01'),
(2, 93.00, '2025-04-01'),
(2, 95.00, '2025-05-01'),
(2, 97.00, '2025-06-01'),
(2, 99.00, '2025-07-01'),
(2, 101.00, '2025-08-01'),

-- Stellar Crown PC ETB
(3, 80.00, '2025-01-01'),
(3, 82.00, '2025-02-01'),
(3, 84.00, '2025-03-01'),
(3, 86.00, '2025-04-01'),
(3, 88.00, '2025-05-01'),
(3, 90.00, '2025-06-01'),
(3, 92.00, '2025-07-01'),
(3, 94.00, '2025-08-01'),

-- Twilight Masquerade PC ETB
(4, 76.00, '2025-01-01'),
(4, 78.00, '2025-02-01'),
(4, 80.00, '2025-03-01'),
(4, 82.00, '2025-04-01'),
(4, 84.00, '2025-05-01'),
(4, 86.00, '2025-06-01'),
(4, 88.00, '2025-07-01'),
(4, 90.00, '2025-08-01');



SELECT COUNT(*) FROM ItemValues;
