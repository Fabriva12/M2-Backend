Este proyecto implementa un backend completo para una tienda, desarrollado con Flask, SQLAlchemy, y PostgreSQL.
El sistema permite manejar usuarios, productos, carritos de compra, ventas y facturas, incluyendo autenticación con JWT (RS256) y validación de roles de usuario.
El propósito principal es simular un entorno real de e-commerce, donde los clientes pueden comprar productos, y los administradores pueden gestionar usuarios, inventario y facturación.

🧩 Arquitectura del Proyecto
El proyecto se divide en 3 módulos principales:

🔐 1. Módulo de Usuarios y Autenticación
Permite registrar usuarios, iniciar sesión y eliminar cuentas.
Implementa JWT con firma RS256 para validar sesiones y roles.
Existen dos roles:
admin: acceso total (usuarios, productos, ventas, devoluciones).
user: acceso limitado (consultas, carritos y compras).

🏷️ 2. Módulo de Productos
Permite crear, actualizar, consultar y eliminar productos.
Mantiene sincronización del stock con el módulo de ventas.
Solo accesible por administradores para modificaciones.


🛒 3. Módulo de Ventas (Carritos y Facturas)
Gestiona carritos de compra, productos asociados y finalización de compras.
Permite consultar facturas y realizar devoluciones, restaurando stock.
Los usuarios pueden revisar sus propios carritos y facturas.


⚙️ Requerimientos Técnicos

Base de datos: PostgreSQL
ORM: SQLAlchemy
Framework Web: Flask
Autenticación: JWT (algoritmo RS256)
Testing: pytest
Cache : Redis

🔑 Generación de Claves para JWT

El proyecto utiliza JWT con firma asimétrica (RS256).
Debes generar dos claves: una privada (para firmar tokens) y una pública (para validarlos).
Ejecuta los siguientes comandos en la terminal:

# Generar clave privada
openssl genrsa -out private.key 2048

# Generar clave pública a partir de la privada
openssl rsa -in private.key -pubout -out public.key

Coloca ambos archivos en la raíz del proyecto