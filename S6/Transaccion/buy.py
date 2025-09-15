from sqlalchemy import insert, update, select
from transaccion_tables import engine, products_table, user_table, bill_table


def transaction_buy_product(product_ID, user_ID, quantity):
    with engine.begin() as conn:
        result = select(products_table).where(products_table.c.ID == product_ID)
        row = conn.execute(result).fetchone()
        if not row or row.stock < quantity:
            print("Sin stock disponible, abortando")
            return
        
        result_2 = select(user_table).where(user_table.c.ID== user_ID)
        row_2 = conn.execute(result_2).fetchone()
        if not row_2:
            print("el usuario no está registrado")
            return
    
        new_bill= insert(bill_table)
        values =[
            {"user_id":user_ID , "product_ID":product_ID , "quantity": quantity}
        ]
        conn.execute(new_bill,values)

        reduce_stock= update(products_table).where(products_table.c.ID == product_ID).values(stock = products_table.c.stock - quantity)
        conn.execute(reduce_stock)

