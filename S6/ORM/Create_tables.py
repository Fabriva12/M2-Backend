from sqlalchemy  import text
from Tables import user_table, cars_table, address_table, engine

def create_tables():
    try: 
        with engine.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS lyfter_cars2 "))

            for tabla in [user_table, cars_table, address_table]:
                if not engine.dialect.has_table(conn,tabla.name, schema='lyfter_cars2' ):
                    print(f"Creando tabla: {tabla.name}")
                    tabla.create(conn)
                    
                else:
                    print(f"La tabla {tabla.name} ya existe, no se crea.")

    except Exception as e:
        print("Connection failed:", e)
