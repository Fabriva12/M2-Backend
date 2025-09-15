from Tables import address_table, engine
from sqlalchemy import insert,select,update, delete

def new_address():
    with engine.connect() as conn:
        stmt=(
            insert(address_table),
            [
                {"user_ID": 2, "address": "Narnia"},
                {"User_ID": 1, "address": "Zarcero"}
            ],
        )
        conn.execute(stmt)
        conn.commit()

def update_address(old_address, new_address):
    with engine.connect() as conn:
        stmt= (
            update(address_table)
            .where(address_table.c.address == old_address)
            .values(address = new_address)
        )
        conn.execute(stmt)
        conn.commit()

# update_address("Zarcero","Tamarindo")

def select_address():
    with engine.connect() as conn:
        stmt = select(address_table)
        result = conn.execute(stmt)          
        for row in result.fetchall():      
            print(row)

def delete_address(address_ID,):
    with engine.connect() as conn:
        stmt= (
            delete(address_table)
            .where(address_table.c.id == address_ID)
        )
        conn.execute(stmt)
        conn.commit()

# delete_address(1)