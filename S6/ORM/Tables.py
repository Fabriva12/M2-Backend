from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

DB = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB, echo=True)
metadata_obj = MetaData(schema= 'lyfter_cars2')


user_table = Table(
		"users",
		metadata_obj,
		Column("id", Integer, primary_key=True),
		Column("name", String(30)),
		Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id"), nullable=False), 
    Column("address", String, nullable=False),
)

cars_table = Table(
    "cars",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("Brand", String(20), nullable= False),
    Column("Model", String(20), nullable= False),
    Column("Year", Integer, nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable= True),
)

