-- SQLite
-- Tabla productos
CREATE TABLE Productos(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Código VARCHAR(10) UNIQUE NOT NULL,
Nombre VARCHAR(25) NOT NULL,
Precio Int DEFAULT 0,
Fecha_de_ingreso VARCHAR(10) NOT NULL,
Marca VARCHAR(25) NOT NULL
);

INSERT INTO Productos(Código, Nombre, Precio,  Fecha_de_Ingreso, Marca)
VALUES
    ("P01", "Cinta", 1000, "19/08/2025", "CCM"),
    ("P02", "Taladro", 65000, "19/08/2025", "Makita"),
    ("P03", "Martillo", 5000, "19/08/2025", "KLH"),
    ("P04", "Aspiradora", 75000, "19/08/2025", "Makita"),
    ("P05", "Tornillos", 1500, "19/08/2025", "SL"),
    ("P06", "Clavos", 1200, "19/08/2025", "SL"),
    ("P07", "Hidrolavadora", 45000, "19/08/2025", "Black"),
    ("P08", "Pintura", 65000, "19/08/2025", "Lanco");


-- Tabla Facturas
CREATE TABLE Facturas(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Número INT UNIQUE NOT NULL,
Fecha VARCHAR(10) NOT NULL,
Correo VARCHAR(30) NOT NULL,
Monto INT NOT NULL,
Telefono Int NOT NULL,
Código_Empleado VARCHAR(5) NOT NULL
);

INSERT INTO Facturas(Número, Fecha, Correo, Monto, Telefono, Código_Empleado)
VALUES
    (  1, "19/08/2025", "ben@gmail.com", 71500, 84735468, "M1"),
    (  2, "19/08/2025", "agapito@gmail.com", 65000, 84238456, "M3"),
    (  3, "19/08/2025", "corageelperro@gmail.com", 5000, 88885488, "M2"),
    (  4, "19/08/2025", "billy@hotmail.com", 55500, 86925671, "M3");

--  Tabla Detalle_Factura
CREATE TABLE Detalle_Factura(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Número_Factura INT NOT NULL,
ID_Producto INT NOT NULL,
Cantidad INT DEFAULT 1,
FOREIGN KEY (Número_Factura) REFERENCES Facturas(Número),
FOREIGN KEY (ID_Producto) REFERENCES Productos(ID)
);

INSERT INTO Detalle_Factura(Número_Factura, ID_Producto, Cantidad)
VALUES
    (1,2,1),
    (1,3,1),
    (1,5,1),
    (2,2,1),
    (3,3,1),
    (4,7,1),
    (4,6,5),
    (4,5,1),
    (4,1,3);

-- Tabla Carrito
CREATE TABLE Carrito(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Email VARCHAR (30) UNIQUE NOT NULL
);

-- Tabla Detalle_Carrito
CREATE TABLE Detalle_Carrito(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
ID_Carrito INT NOT NULL,
Código_Producto INT NOT NULL,
Cantidad INT DEFAULT 1,
FOREIGN KEY (ID_Carrito) REFERENCES Carrito(ID),
FOREIGN KEY (Código_Producto) REFERENCES Productos(Código)
);