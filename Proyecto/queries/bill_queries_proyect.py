from sqlalchemy import and_, select, update 
from create_tables_proyect import engine, product_table, cart_items_table, bill_table

class Bill_DB:
    def __init__(self):
        self.engine = engine
    
    # Con esta funcion creamos el query para ver la factura deseada
    def view_bills(self, user_ID,cart_ID=None):
        with engine.connect() as conn:
            stmt= select(bill_table).where(and_(bill_table.c.user_ID == user_ID, bill_table.c.cart_ID == cart_ID if cart_ID else True))
            result = conn.execute(stmt)
        
            rows = [dict(row) for row in result.mappings()]
            return rows


    # Con la siguiente funcion creamos el query para devolver la factura y hacer los cambios en la base de datos
    def return_bill(self, bill_ID):
        with engine.begin() as conn:
            result = select(bill_table).where(bill_table.c.ID == bill_ID)
            row = conn.execute(result).mappings().first() 
            if not row:
                return "Factura no encontrada"
            cart_ID= row['cart_ID']
            items_query = select(cart_items_table).where(cart_items_table.c.cart_ID == cart_ID)
            items = conn.execute(items_query).mappings().all()
            for item in items:
                product_ID= item['product_ID']
                quantity= item['quantity']
                stock_query = select(product_table.c.stock).where(product_table.c.ID == product_ID)
                current_stock = conn.execute(stock_query).scalar_one()
                update_stock= update(product_table).where(product_table.c.ID == product_ID).values(stock = current_stock + quantity)
                conn.execute(update_stock)
            update_bill= update(bill_table).where(bill_table.c.ID == bill_ID).values(state = 'devuelta')
            conn.execute(update_bill)
            return "Factura devuelta correctamente"