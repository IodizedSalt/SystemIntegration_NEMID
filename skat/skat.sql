-- SQLite
-- f1, open database

DROP TABLE users

CREATE TABLE IF NOT EXISTS users(
    email TEXT,
    balance INTEGER
)

INSERT INTO users VALUES('a@a.com', 238.45);
INSERT INTO users VALUES('b@b.com', 987.23);


SELECT * from users

