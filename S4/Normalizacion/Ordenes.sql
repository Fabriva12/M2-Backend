-- SQLite
-- La primera división que hice fue hacer una tabla llamada clientes, ya que se repiten clientes y tenemos redundancias innecesarias
CREATE TABLE Customers(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Customer_Name VARCHAR(25) NOT NULL,
Customer_Phone Int DEFAULT 0,
Address VARCHAR UNIQUE NOT NULL
);

-- La segunda tabla que cree fue de Items evitando dependencia indirecta
CREATE TABLE Items(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Item_Name VARCHAR(15) NOT NULL,
Price Int DEFAULT 0
);

-- Cree la tabla ordenes la cual esta enlazada unicamente con el ID del cliente
CREATE TABLE Orders(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Customer_ID INT,
Delivery_time VARCHAR(7) NOT NULL,
FOREIGN KEY (ID_CUSTOMER) REFERENCES Customers(ID)
);

-- Por ultimo la tabla Detail_Orden en la cual enlazamos a Item y Orders
CREATE TABLE Detail_Orders(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ID_Orders INT,
ID_Item INT,
Quantity INT  DEFAULT 1,
Special_Request VARCHAR DEFAULT NONE,
FOREIGN KEY (ID_Orders) REFERENCES Orders(ID)
FOREIGN KEY (ID_Item) REFERENCES Items(ID)
);

-- Al añadir los clientes me di cuenta que Claire tenia 2 direcciones por lo que tuve que crear una tabla nueva
CREATE TABLE Address(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Customer_ID INT,
Address VARCHAR (40),
FOREIGN KEY (Customer_ID) REFERENCES Customers(ID)
);

-- Tambien tuve que agregar Adress_ID a Orders
ALTER TABLE Orders ADD COLUMN Address_ID INTEGER REFERENCES Address(ID);

--No logré elimiar Adress de Customers por lo que elimine la tabla completa y la volvi a crear sin Adresscha
DROP TABLE Customers;

CREATE TABLE Customers(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Customer_Name VARCHAR(25) NOT NULL,
Customer_Phone INT NOT NULL
);

-- Agregué primeramente los customers
INSERT INTO Customers(Customer_Name, Customer_Phone)
VALUES
    ("Alice", 1234567890),
    ("Bob", 9876543210),
    ("Claire", 5551234567);

-- Agregué los items
INSERT INTO Items(Item_Name, Price)
VALUES
    ("Cheeseburger", 4),
    ("Fries", 1 ),
    ("Pizza", 10 ),
    ("Salad", 6),
    ("Water", 1);

-- Cuando estaba agregando los items encontre que los especial request tenian valor tambien por lo que tuve que crear una tabla y modificando Detail_Order 
CREATE TABLE  Special_Request(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Request VARCHAR (20) NOT NULL,
Price Smallint NOT NULL
);

DROP tABLE Detail_Orders;

CREATE TABLE Detail_Orders(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ID_Orders INT,
ID_Item INT,
Quantity INT  DEFAULT 1,
ID_Special_Request INT,
FOREIGN KEY (ID_Orders) REFERENCES Orders(ID)
FOREIGN KEY (ID_Item) REFERENCES Items(ID)
FOREIGN KEY (ID_Special_Request) REFERENCES Special_Request(ID)
);

-- Agregué Special Request
INSERT INTO Special_Request(Request, Price)
VALUES
    ("No onions", 0),
    ("Extra Ketchup", 2),
    ("Extra Cheese", 2),
    ("No croutons", 0),
    ("None", 0);

--  Agregué Address
INSERT INTO Address(Customer_ID, Address)
VALUES
    (1,"123 Main St"),
    (2,"456 Elm St"),
    (3,"789 Oak St"),
    (3,"464 Georgia St");

-- Agregué Orders
INSERT INTO Orders(Customer_ID, Delivery_time, Address_ID)
VALUES
    (1,"6:00pm", 1),
    (1,"6:00pm",1),
    (2,"7:30pm",2),
    (2,"7:30pm", 2),
    (3,"12:00pm",3),
    (4,"5:00pm",4);

-- Agregué Details_Order
INSERT INTO Detail_Orders(ID_Orders, ID_Item, Quantity, ID_Special_Request)
VALUES
    (1,1,2,1),
    (2,2,1,2),
    (3,3,1,3),
    (4,2,2,5),
    (5,4,1,4),
    (6,5,1,5);