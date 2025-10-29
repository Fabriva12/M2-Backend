from sqlalchemy import insert, select, update 
from create_tables_proyect import engine, product_table, cart_items_table, cart_table, bill_table


# con esta clase manejamos las consultas de compras a la base de datos
class Buy_DB:
    def __init__(self):
        self.engine = engine
        
    def new_cart(self,user_ID, product_ID, quantity):
        with engine.begin() as conn:
            result = select(product_table).where(product_table.c.ID == product_ID)
            row = conn.execute(result).mappings().first() 
            if not row:
                print("Producto no encontrado")
            new_cart= insert(cart_table).returning(cart_table.c.ID).values(user_ID=user_ID, Total= row["price"] * quantity)
            cart_result = conn.execute(new_cart)
            cart_id = cart_result.scalar_one()

            new_item= insert(cart_items_table).values(cart_ID=cart_id, product_ID=product_ID, quantity=quantity)
            conn.execute(new_item)


    def add_items_cart(self, cart_ID, product_ID, quantity):
        with engine.begin() as conn:
            result = select(product_table).where(product_table.c.ID == product_ID)
            row = conn.execute(result).mappings().first() 
            if not row:
                print("Producto no encontrado")

            new_item= insert(cart_items_table).values(cart_ID=cart_ID, product_ID=product_ID, quantity=quantity)
            conn.execute(new_item)
            update_total= update(cart_table).where(cart_table.c.ID == cart_ID).values(Total = cart_table.c.Total + (row["price"] * quantity))
            conn.execute(update_total)


    def see_my_carts(self, user_ID,):
        with engine.begin() as conn:
            result = select(cart_table).where(cart_table.c.user_ID == user_ID)
            rows = conn.execute(result).mappings().all() 
            return ([dict(row) for row in rows])


    def view_cart_items(self, cart_ID,):
        with engine.begin() as conn:
            result = select(cart_items_table).where(cart_items_table.c.cart_ID == cart_ID)
            rows = conn.execute(result).mappings().all() 
            return ([dict(row) for row in rows])
        
    
    
    def buy_cart(self,user_ID, cart_ID, address, payment_method):
        with engine.begin() as conn:
            items_query = select(cart_items_table).where(cart_items_table.c.cart_ID == cart_ID)
            items = conn.execute(items_query).mappings().all()
            for item in items:
                stock_query = select(product_table.c.stock).where(product_table.c.ID == item['product_ID'])
                current_stock = conn.execute(stock_query).scalar_one()
            
                if current_stock < item['quantity']:
                    print(f"No hay suficiente stock para el producto ID: {item['product_ID']}")
                    return 
            
            for item in items:
                update_stock = (update(product_table).where(product_table.c.ID == item['product_ID']).values(stock = product_table.c.stock - item['quantity']))
                conn.execute(update_stock)

            conn.execute(update(cart_table).where(cart_table.c.ID == cart_ID).values(state='COMPLETED'))

            total_query = select(cart_table.c.Total).where(cart_table.c.ID == cart_ID)
            total_value = conn.execute(total_query).scalar_one()

            conn.execute(insert(bill_table).values(user_ID=user_ID, cart_ID=cart_ID, Total=total_value, address=address, payment_method=payment_method))

        print(f"Compra completada para el carrito {cart_ID}. Factura generada.")