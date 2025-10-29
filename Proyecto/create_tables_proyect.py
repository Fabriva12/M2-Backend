from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text, Date, func

# creamos la conexion a la base de datos
DB = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB, echo=True,pool_size=10,max_overflow=5,pool_recycle=180)
metadata_obj = MetaData(schema= 'lyfter_bk_project')

# con la siguiente funcion creamos las tablas para nuestra base de danos en postgres si no existen
def create_tables(): 
    try: 
        with engine.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS lyfter_bk_project "))

            for tabla in [product_table, user_table,cart_table,cart_items_table, bill_table]:
                if not engine.dialect.has_table(conn,tabla.name, schema='lyfter_bk_project' ):
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
    Column("SKU",String(10),unique=True),
    Column("price",Integer),
    Column("date",Date, server_default=func.current_date()),
    Column("stock",Integer)
)

user_table = Table(
    "user_table",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("email",String(30), unique=True),
    Column("password",String(25)),
    Column("role",String(25))
)


cart_table = Table(
    "cart_table",
    metadata_obj,
    Column("ID", Integer, primary_key= True),
    Column("user_ID",Integer, ForeignKey("user_table.ID")),
    Column("state",String(25), server_default=text("'open'")),
    Column("Total", Integer)
)

cart_items_table = Table(
    "cart_items_table",
    metadata_obj,
    Column("ID", Integer, primary_key= True),
    Column("cart_ID", Integer, ForeignKey("cart_table.ID")),
    Column("product_ID", Integer, ForeignKey("product_table.ID")),
    Column("quantity", Integer)
)

bill_table = Table(
    "bill_table",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("user_ID", Integer, ForeignKey("user_table.ID")),
    Column("address", String(100)),
    Column("cart_ID", Integer, ForeignKey("cart_table.ID")),
    Column("Total", Integer),
    Column("payment_method", String(25)),
    Column("create", Date, server_default=func.current_date()),
    Column("state",String(25), server_default=text("'emitida'"))
)

create_tables()