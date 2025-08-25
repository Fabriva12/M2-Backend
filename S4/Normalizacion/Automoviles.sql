-- Primeramente cree la tabla Vehicle
CREATE TABLE Vehicle(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
VIN VARCHAR (11) NOT NULL UNIQUE,
Make VARCHAR (15) NOT NULL,
Model VARCHAR (15) NOT NULL,
Year SMALLINT NOT NULL
);

-- Luego la tabla Owner
CREATE TABLE Owner(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR (30) NOT NULL,
Phone INT UNIQUE NOT NULL
);

-- Y la tabla Insurance
CREATE TABLE Owner(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR (30) NOT NULL,
Phone INT UNIQUE NOT NULL,
Vehicle_ID INT NOT NULL,
FOREIGN KEY (Vehicle_ID) REFERENCES Vehicle(ID)
);

-- Cree otra tabla Car_Owner ya que un vehiculo puede tener varios dueños y un dueño varios vehiculos
CREATE TABLE Car_Owner(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Vehicle_ID INT NOT NULL,
Owner_ID INT NOT NULL,
FOREIGN KEY (Vehicle_ID) REFERENCES Vehicle(ID),
FOREIGN KEY (Owner_ID) REFERENCES Owner(ID)
);

-- Iba a agregar los vehiculos y noté que no agregué color a la tabla
ALTER TABLE Vehicle
ADD Color VARCHAR(10) ;

-- Agregué los valores de vehicle
INSERT INTO Vehicle(VIN, Make, Model, Year, Color)
VALUES
    ("1HGCM82633A", "Honda", "Accord", 2003, "Silver"),
    ("5J6RM4H79EL", "Honda", "CRV", 2014, "Blue"),
    ("1G1RA6EH1FU", "Chevrolet", "Volt", 2015, "Red");


-- Agregué los Owner
INSERT INTO Owner(Name, Phone)
VALUES
    ("Alice", 1234567890),
    ("Bob", 9876543210),
    ("Claire", 5551234567),
    ("Dave", 1112223333);

-- Agregué Insurance
INSERT INTO Insurance(Insurance_Company, Insurance_Policy, Vehicle_ID)
VALUES
    ("ABC Insurance", "POL12345", 1),
    ("XYZ Insurance", "POL54321", 1),
    ("DEF Insurance", "POL67890", 2),
    ("GHI Insurance", "POL98765", 3);

-- Agregué Car_Owner
INSERT INTO Car_Owner(Owner_ID, Vehicle_ID)
VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3);