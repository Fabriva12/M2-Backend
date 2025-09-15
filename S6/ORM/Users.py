from Tables import user_table, engine
from sqlalchemy import insert,select,update, delete

def new_user():
    with engine.connect() as conn:
        stmt=(
            insert(user_table),
            [
                {"name": "Ben", "fullname": "Tenison"},
                {"name": "John", "fullname": "Snow"}
            ],
        )
        conn.execute(stmt)
        conn.commit()

def update_user(old_name, new_name):
    with engine.connect() as conn:
        stmt= (
            update(user_table)
            .where(user_table.c.name == old_name)
            .values(name = new_name)
        )
        conn.execute(stmt)
        conn.commit()

# update_user("Ben","Wen")

def select_user():
    with engine.connect() as conn:
        stmt = select(user_table)
        result = conn.execute(stmt)          
        for row in result.fetchall():        
            print(row)

def delete_user(user_ID,):
    with engine.connect() as conn:
        stmt= (
            delete(user_table)
            .where(user_table.c.id == user_ID)
        )
        conn.execute(stmt)
        conn.commit()

# delete_user(1)