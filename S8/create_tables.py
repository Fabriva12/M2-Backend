from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text, Date, func

DB = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB, echo=True)
metadata_obj = MetaData(schema= 'lyfter_verduleria')


def create_tables():
    try: 
        with engine.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS lyfter_verduleria "))

            for tabla in [product_table, user_table, bill_table]:
                if not engine.dialect.has_table(conn,tabla.name, schema='lyfter_verduleria' ):
                    print(f"Creando tabla: {tabla.name}")
                    tabla.create(conn)
                    
                else:
                    print(f"La tabla {tabla.name} ya existe, no se crea.")

    except Exception as e:
        print("Connection failed:", e)



product_table = Table(
    "product_table",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("name",String(25) ),
    Column("price",Integer),
    Column("date",Date, server_default=func.current_date()),
    Column("stock",Integer)
)

user_table = Table(
    "user_table",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("user",String(25)),
    Column("password",String(25)),
    Column("state",String(25))
)


bill_table = Table(
    "bill_table",
    metadata_obj,
    Column("ID", Integer, primary_key= True),
    Column("user_ID",Integer, ForeignKey("user_table.ID")),
    Column("product_ID",Integer, ForeignKey("product_table.ID")),
    Column("quantity",Integer),
    Column("Total", Integer),
    Column("State", String(25))
)

create_tables()