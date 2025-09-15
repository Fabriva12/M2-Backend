from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, Integer, String

DB= 'postgresql://postgres:postgres@localhost:5432/postgres'
engine= create_engine(DB, echo=True)
metadata_obj = MetaData("lyfter_product")

products_table = Table(
    "products",
    metadata_obj,
    Column("ID", Integer, primary_key= True),
    Column("name", String(30)),
    Column("code", String(10)),
    Column("stock", Integer),
)

user_table = Table(
    "user",
    metadata_obj,
    Column("ID", Integer, primary_key=True),
    Column("name", String(30)),
)

bill_table = Table(
    "bill",
    metadata_obj,
    Column("ID", Integer, primary_key= True),
    Column("user_ID", ForeignKey("user.ID")),
    Column("product_ID", ForeignKey("products.ID")),
    Column("quantity", Integer),
    Column("state", String(15))
)