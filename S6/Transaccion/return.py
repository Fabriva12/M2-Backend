from sqlalchemy import select,update, insert
from transaccion_tables import engine, bill_table, products_table

def return_product(bill_ID):
    with engine.begin() as conn:
        slt_bill = select(bill_table.c.product_ID, bill_table.c.quantity).where(bill_table.c.ID == bill_ID )
        row = conn.execute(slt_bill).fetchone()
        if not row:
            return
        quantity = row.quantity
        product_ID = row.product_ID 
        updt_products= update(products_table).where(products_table.c.ID == product_ID).values(stock= products_table.c.stock + quantity)
        conn.execute(updt_products)

        updt_bill= update(bill_table).where(bill_table.c.ID == bill_ID ).values(state = "Retornada")
        conn.execute(updt_bill)

return_product(1)
