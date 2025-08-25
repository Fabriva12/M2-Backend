-- SQLite
-- 1-Obtenga todos los productos almacenados
SELECT * from Productos

-- 2-Obtenga todos los productos que tengan un precio mayor a 50000
SELECT * from Productos
WHERE Precio >50000;

-- 3-Obtenga todas las compras de un mismo producto por id.
SELECT f.Número, f.Fecha, d.ID_Producto, d.Cantidad
FROM Facturas f
JOIN Detalle_Factura d
    ON f.Número = d.Número_Factura
WHERE d.ID_Producto = 5;

-- 4-Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT p.Nombre, p.Precio, d.ID_Producto, sum(d.Cantidad) AS Total_comprado
FROM Productos p
JOIN Detalle_Factura d
    ON p.ID = d.ID_Producto
GROUP BY d.ID_Producto, p.Nombre;

-- 5-Obtenga todas las facturas realizadas por el mismo comprador
SELECT Correo, Monto, Número
FROM Facturas 
WHERE Correo == "ben@gmail.com";

-- 6-Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * FROM Facturas 
ORDER BY Monto DESC;

-- 7-Obtenga una sola factura por número de factura
SELECT * FROM Facturas 
Where Número ==1;