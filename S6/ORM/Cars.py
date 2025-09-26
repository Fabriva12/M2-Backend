from Tables import cars_table, engine
from sqlalchemy import insert,select,update, delete

def new_car():
    with engine.connect() as conn:
        stmt=(
            insert(cars_table),
            [
                {"Brand": "Hyundai", "Model": "Tucson", "Year": 2018, "user_id": 1},
                {"Brand": "Toyota", "Model": "Tucson", "Year": 2018, "user_id": 2},
            ],
        )
        conn.execute(stmt)
        conn.commit()


def update_car(old_model, new_model):
    with engine.connect() as conn:
        stmt= (
            update(cars_table)
            .where(cars_table.c.model == old_model)
            .values(name = new_model)
        )
        conn.execute(stmt)
        conn.commit()

# update_car("Yaris","Rav4")

def insert_car_user(car_ID, new_user):
    with engine.connect() as conn:
        stmt= (
            update(cars_table)
            .where(cars_table.c.id == car_ID)
            .values(user_id = new_user)
        )
        conn.execute(stmt)
        conn.commit()
# insert_car_user(1,3)

def select_car():
    with engine.connect() as conn:
        stmt = select(cars_table)
        result = conn.execute(stmt)          
        for row in result.fetchall():        
            print(row)

def delete_car(car_ID,):
    with engine.connect() as conn:
        stmt= (
            delete(cars_table)
            .where(cars_table.c.id == car_ID)
        )
        conn.execute(stmt)
        conn.commit()

# delete_car(1)