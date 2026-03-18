import psycopg2


def connect_to_db():
    """Функция для соединения с БД"""
    conn = psycopg2.connect(
        host='localhost',
        database='sfmshop',
        user='vladislav',
        password=''
    )
    return conn



def get_orders_with_products(conn, user_id):
    """Получить заказы пользователя с товарами"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    orders.id, 
                    products.name, 
                    order_items.quantity,
                    order_items.price
                FROM orders
                INNER JOIN order_items ON orders.id = order_items.order_id
                INNER JOIN products ON order_items.product_id = products.id
                WHERE orders.user_id = %s
            """, (user_id,))
            results = cursor.fetchall()
            cursor.close()
            return results
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')

def get_order_statistics(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_id, COUNT(*) as order_count, SUM(total) as total_sum
        FROM orders
        GROUP BY user_id
        ORDER BY total_sum DESC
    """)
    results = cursor.fetchall()
    cursor.close()
    return results


if __name__ == '__main__':
    print(get_orders_with_products(connect_to_db(), 2))
    print(get_order_statistics(connect_to_db()))