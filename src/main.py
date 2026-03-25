import src.database.connection as sdc
import src.database.queries as sdq


conn = sdc.connect_to_db()

sdc.create_user(conn, 'Дмитрий', 'arbittr885@email.com')
sdc.get_all_products(conn)
print(sdq.get_order_statistics(conn))
print(sdq.get_top_products(conn))
print(sdc.get_user_by_id(conn, 1))
print(sdc.delete_order(conn, 1))

