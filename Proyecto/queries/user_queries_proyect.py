from sqlalchemy import insert, select
from create_tables_proyect import engine, user_table


# con esta clase manejamos las consultas de usuarios a la base de datos
class User_DB:
    def __init__(self):
        self.engine = engine
        
    def insert_user(self, email, password, role):
        stmt = insert(user_table).returning(user_table.c.ID, user_table.c.role).values(email=email, password=password, role=role)
        with self.engine.begin() as conn:
            conn.execute(stmt)
        
        

    def get_user(self, email, password):
        stmt = select(user_table).where(user_table.c.email == email, user_table.c.password == password)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result) if result else None


    def delete_user(self, user_ID):
        with self.engine.begin() as conn:
            delete_user= user_table.delete().where(user_table.c.ID == user_ID)
            conn.execute(delete_user)

    