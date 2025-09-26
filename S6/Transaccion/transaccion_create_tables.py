from sqlalchemy import text, insert, values
from transaccion_tables import products_table, user_table, bill_table, engine

def create_tables():
    try:
        with engine.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS lyfter_product"))
            
            for tabla in [products_table, user_table, bill_table]:
                if not engine.dialect.has_table(conn, tabla.name, schema= "lyfter_product"):
                    print(f"Creando tabla: {tabla.name}")
                    tabla.create(conn)
                    
                else:
                    print(f"La tabla {tabla.name} ya existe, no se crea.")

    except Exception as e:
        print("Connection failed:", e)


def create_product():
    with engine.connect() as conn:
        stmt =insert(products_table)
        values=[
            {"name": "tenis" ,"code":"P04" , "stock":5 },
            {"name": "camiseta","code":"P01" , "stock":3 },
            {"name": "pantaloneta","code":"P03" , "stock":8 }
            ]
        conn.execute(stmt, values)
        conn.commit()

def create_user():
    with engine.connect() as conn:
        stmt =insert(user_table)
        values=[
            {"name": "Pedro Fernandez"  },
            {"name": "Julieta Venegas" },
            ]
        conn.execute(stmt, values)
        conn.commit()

create_tables()
