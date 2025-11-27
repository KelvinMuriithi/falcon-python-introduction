CREATE DATABASE falcon;
CREATE TABLE users(
    id primary key,AUTOINCREMENT
    name TEXT,
    email TEXT,
   );
    CREATE TABLE customers (
    id primary key,
    user_id INTEGER,
    CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    

