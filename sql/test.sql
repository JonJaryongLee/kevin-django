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
