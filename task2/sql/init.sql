CREATE TABLE IF NOT EXISTS full_names (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    status BOOLEAN DEFAULT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS name_with_out_exist ON full_names((split_part(name, '.', 1)));

CREATE TABLE IF NOT EXISTS short_names (
    name VARCHAR(255) NOT NULL PRIMARY KEY UNIQUE,
    status BOOLEAN NOT NULL
);

TRUNCATE TABLE full_names;
TRUNCATE TABLE short_names;