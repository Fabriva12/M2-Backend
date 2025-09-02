-- Tabla Authors
CREATE TABLE Authors(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(25) NOT NULL
);

INSERT INTO Authors(Name)
VALUES
    ("Miguel de Cervantes"),
    ("Dante Alighieri"),
    ("Takehiko Inoue"),
    ("Akira Toriyama"),
    ("Walt Disney");

-- Tabla Customers
CREATE TABLE Customers(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(25) NOT NULL,
Email VARCHAR(25) NOT NULL
);

INSERT INTO Customers(Name, Email)
VALUES
    ("John Doe", "j.doe@email.com"),
    ("Jane Doe", "jane@doe.com"),
    ("3	Luke Skywalker", "darth.son@email.com");

-- Tabla Books
CREATE TABLE Books(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(25) NOT NULL,
Author_ID int DEFAULT NULL,
FOREIGN KEY (Author_ID) REFERENCES Authors(ID)

INSERT INTO Books(Name, Author_ID)
VALUES
    ("Don Quijote", 1),
    ("La Divina Comedia", 2),
    ("Vagabond 1-3", 3),
    ("Dragon Ball 1", 4),
    ("The Book of the 5 Rings" NULL);

-- Tabla Rents
CREATE TABLE Rents(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Book_ID INT NOT NULL,
Customer_ID INT NOT NULL,
State VARCHAR(8) NOT NULL,
FOREIGN KEY (Customer_ID) REFERENCES Customers(ID),
FOREIGN KEY (Book_ID) REFERENCES Books(ID)
);

INSERT INTO Rents(Book_ID, Customer_ID, State)
VALUES
    (1, 2, "Returned"),
    (2, 2, "Returned"),
    (1, 1, "On Time"),
    (3, 1, "On Time"),
    (2, 2, "Overdue");

-- Obtenga todos los libros y sus autores
SELECT b.Name, a.Name AS Author
From Books b
LEFT JOIN Authors a ON a.ID = b.Author_ID;

-- Obtenga todos los libros que no tienen autor
SELECT b.Name, a.Name AS Author
From Books b
LEFT JOIN Authors a ON a.ID = b.Author_ID
WHERE a.Name is NULL

-- Obtenga todos los autores que no tienen libros
SELECT a.Name, b.Name AS Book
From Authors a
LEFT JOIN Books b ON b.Author_ID = a.ID
WHERE b.Author_ID is NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT b.Name , r.State
From Rents r
LEFT JOIN Books b ON b.ID = r.Book_ID

-- Obtenga todos los libros que nunca han sido rentados
SELECT b.Name 
From Books b
LEFT JOIN Rents r ON r.Book_ID = b.ID 
WHERE r.Book_ID IS NULL;

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT c.Name 
From Customers c
LEFT JOIN Rents r ON r.Customer_ID = c.ID 
WHERE r.Customer_ID IS NULL;

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT b.Name , r.State
From Rents r
LEFT JOIN Books b ON b.ID = r.Book_ID
WHERE r.State = "Overdue";
