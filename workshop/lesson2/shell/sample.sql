/*
    This is a sample file used for Topic 12 (Django shell).

    There is nothing to do here with Django, but just to emphasize on
    how Django ORMs is helping us a lot so we do not have to write
    plain SQL syntax like this.

    See `shell.py` for Django's queryset API reference.
*/

-- create table
CREATE TABLE lesson (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
);

-- create operation (C)
INSERT INTO lesson (name, score) VALUES ("math", 70);
INSERT INTO lesson (name, score) VALUES ("english", 77);
INSERT INTO lesson (name, score) VALUES ("physics", 82);

-- read operation (R)
SELECT * FROM lesson;
SELECT * FROM lesson WHERE score < 80;
SELECT score FROM lesson WHERE name = "math";

-- update operation (U)
UPDATE lesson SET score = 83 WHERE name = "physics";

-- delete operation (D)
DELETE FROM lesson WHERE name = "english";
