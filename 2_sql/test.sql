CREATE TABLE classmates (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL UNIQUE
);

INSERT INTO classmates (name, age, email)
VALUES 
    ('jony', 30, 'jony@email.com'),
    ('sylvie', 24, 'tarrie@hotmail.com'),
    ('nana', 4, 'nanana@naver.com');

CREATE TABLE users (
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	age INTEGER NOT NULL,
	country TEXT NOT NULL,
	phone TEXT NOT NULL,
	balance INTEGER NOT NULL
);

SELECT DISTINCT country FROM users;