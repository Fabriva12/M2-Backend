-- Un script que agregue un usuario nuevo
INSERT INTO lyfter_car_rental.users (name, birthdate, email, pasword, username, count_state) 
VALUES 
    ('Fabricio Vargas', '1999-10-12', 'fabricio.12@live.com', 'qw123!', 'Fabriva12', 'active');

-- Un script que agregue un automovil nuevo
insert into lyfter_car_rental.Cars(Brand, Model, Year, State) 
values 
    ('Toyota', 'Hilux', 2018, 'available')

-- Un script que cambie el estado de un usuario
UPDATE lyfter_car_rental.Users
SET count_state = 'inactive'
Where ID =51;

-- Un script que cambie el estado de un automovil
UPDATE lyfter_car_rental.Cars
SET state = 'rented'
Where ID =51;

-- Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
INSERT INTO lyfter_car_rental.Rent_Cars(User_ID, Car_ID, State)
VALUES
    (2,5, 'Rented')

-- Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler
BEGIN;

UPDATE lyfter_car_rental.Cars
SET state = 'available'
Where ID =5;

UPDATE lyfter_car_rental.Rent_Cars
SET state = 'completed'
Where ID =1;

COMMIT;

-- Un script que deshabilite un automovil del alquiler
UPDATE lyfter_car_rental.Cars
SET state = 'disabled'
Where ID =5;

-- Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles. 
SELECT id, model, state
FROM lyfter_car_rental.cars
WHERE state IN ('rented', 'available')
ORDER BY state;