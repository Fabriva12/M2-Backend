from sqlalchemy import create_engine,insert, select, MetaData, update 
from create_tables import engine, user_table, bill_table, product_table

metadata_obj = MetaData()

class DB_Manager:
    def __init__(self):
        self.engine = engine
        
    def insert_user(self, user, password, state):
        stmt = insert(user_table).returning(user_table.c.ID, user_table.c.state).values(user=user, password=password, state=state)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().first()
        return dict(result)

    def get_user(self, user, password):
        stmt = select(user_table).where(user_table.c.user == user, user_table.c.password == password)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result)


    def insert_product(self,name,price,stock):
        with self.engine.begin() as conn:
            new_product= insert(product_table)
            values= [
                {"name":name, "price":price, "stock":stock}
            ]
            conn.execute(new_product,values)


    def delete_product(self, product_ID):
        with self.engine.begin() as conn:
            delete_product= product_table.delete().where(product_table.c.ID == product_ID)
            conn.execute(delete_product)


    def get_product(self, product_ID):
        stmt= select(product_table).where(product_table.c.ID == product_ID)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result)


    def update_product(self,product_ID,data):
        allowed_fields = {"name", "price", "stock"}
        update_data = {k: v for k, v in data.items() if k in allowed_fields}
        if not update_data:
            return
        with self.engine.begin() as conn:
            update_product= update(product_table).where(product_table.c.ID == product_ID)
            values= [
                {**update_data}
            ]
            conn.execute(update_product,values)


    def buy(self,user_ID, product_ID, quantity):
        with engine.begin() as conn:
            result = select(product_table).where(product_table.c.ID == product_ID)
            row = conn.execute(result).mappings().first() 
            if not row:
                print("Producto no encontrado")
            if row["stock"] < quantity:
                print("Sin stock disponible, abortando")
                return
            total = row["price"] * quantity
    
            new_bill= insert(bill_table)
            values =[
                {"user_ID":user_ID , "product_ID":product_ID , "quantity": quantity, "Total":total}
            ]
            conn.execute(new_bill,values)

            reduce_stock= update(product_table).where(product_table.c.ID == product_ID).values(stock = product_table.c.stock - quantity)
            conn.execute(reduce_stock)

    def get_bills(self):
        stmt= select(bill_table)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().all()
            return [dict(row) for row in result]
    
    def get_bills_by_ID(self,user_ID):
        stmt= select(bill_table).where(bill_table.c.user_ID == user_ID)
        with self.engine.begin() as conn:
            result = conn.execute(stmt).mappings().all()
            return [dict(row) for row in result]
        

    def delete_bills(self, user_ID):
        with self.engine.begin() as conn:
            delete_bill= bill_table.delete().where(bill_table.c.user_ID == user_ID)
            conn.execute(delete_bill)

    
    def return_product(bill_ID):
        with engine.begin() as conn:
            slt_bill = select(bill_table.c.product_ID, bill_table.c.quantity).where(bill_table.c.ID == bill_ID )
            row = conn.execute(slt_bill).fetchone()
            if not row:
                return
            quantity = row.quantity
            product_ID = row.product_ID 
            updt_products= update(product_table).where(product_table.c.ID == product_ID).values(stock= product_table.c.stock + quantity)
            conn.execute(updt_products)

            updt_bill= update(bill_table).where(bill_table.c.ID == bill_ID ).values(state = "Retornada")
            conn.execute(updt_bill)