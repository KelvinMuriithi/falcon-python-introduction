# .schema
# CREATE TABLE students (
#   id INTEGER PRIMARY KEY,
#   name TEXT,
#   age INTEGER
# );

# ALTER TABLE students ADD COLUMN email TEXT;
# INSERT INTO students (name, age) VALUES ('Jane Doe', 3, );
# SELECT * FROM students;
# SELECT name, age FROM students;
# SELECT * FROM students WHERE age < 2;
# UPDATE students SET name = "Hana" WHERE name = "Hannah";
# DELETE FROM students WHERE id = 3;
# SELECT * FROM students ORDER BY age;
# SELECT * FROM students ORDER BY age DESC;
# SELECT * FROM students ORDER BY age DESC LIMIT 1;
# SELECT name FROM students WHERE age BETWEEN 1 AND 3;
# SELECT * FROM students WHERE name IS NULL;
# SELECT COUNT(owner_id) FROM students WHERE owner_id = 1;
# SELECT breed, COUNT(breed) FROM students GROUP BY breed;
CREATE TABLE customers(
    id primary key,
    user_id INTEGER,
    CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );