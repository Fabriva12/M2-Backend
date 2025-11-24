from sqlalchemy import insert, select, update 
from create_tables_proyect import engine, product_table


# con esta clase manejamos las consultas de productos a la base de datos
class Product_DB:
    def __init__(self):
        self.engine = engine
        
    def insert_product(self,name,SKU,price,stock):
        with self.engine.begin() as conn:
            new_product= insert(product_table)
            values= [
                {"name":name, "price":price, "stock":stock, "SKU":SKU}
            ]
            conn.execute(new_product,values)


    def get_product(self, product_ID):
        stmt= select(product_table).where(product_table.c.ID == product_ID)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result)


    def delete_product(self, product_ID):
        with self.engine.begin() as conn:
            delete_product= product_table.delete().where(product_table.c.ID == product_ID)
            conn.execute(delete_product) 


    def update_product(self,product_ID,update_data):
        allowed_fields = {"name", "price", "stock", "SKU"}
        new_data = {k: v for k, v in update_data.items() if k in allowed_fields}

        if not new_data:
            return False
        try:
            with self.engine.begin() as conn:
                stmt = (
                    update(product_table)
                    .where(product_table.c.ID == product_ID)
                    .values(**new_data)
                )
                conn.execute(stmt)
        except Exception as e:
            print("error en upgrade")