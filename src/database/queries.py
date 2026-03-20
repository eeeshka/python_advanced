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
    """Получает статистику по пользователям (количество заказов, общая сумма)"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT users.name, COUNT(order_items.id), SUM(order_items.price * order_items.quantity) AS total_sum FROM users
            LEFT JOIN orders ON users.id = orders.user_id
            LEFT JOIN order_items ON orders.id = order_items.order_id
            GROUP BY users.name""")
            results = cursor.fetchall()
            return results
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')

def get_user_order_history(conn, user_id):
    """Получает историю заказов пользователя с информацией о товарах"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT users.name, orders.total, products.name, products.price FROM users
            INNER JOIN orders ON users.id = orders.user_id
            INNER JOIN order_items ON orders.id = order_items.order_id
            INNER JOIN products ON order_items.product_id = products.id
            WHERE users.id = %s
            ORDER BY orders.created_at DESC
            """, (user_id, ))
            result = cursor.fetchall()
            return result
    except psycopg2.Error as e:
        print(f'Ошибка БД: {e}')

def get_top_products(conn, limit=5):
    """Получить топ товаров по количеству продаж"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT
            products.name,
            SUM(order_items.quantity) as total_price
            FROM products
            INNER JOIN order_items ON products.id = order_items.product_id
            GROUP BY products.id, products.name
            ORDER BY total_price DESC
            LIMIT %s""", (limit, ))
            result = cursor.fetchall()
            return result
    except psycopg2.Error as e:
        print(f'Ошибка БД: {e}')


