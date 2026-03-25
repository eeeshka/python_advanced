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


def add_product(conn, name: str, price: int | float, quantity: int):
    """Добавление нового товара в БД"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
                           (name, price, quantity))
            conn.commit()
            return print(f'Добавлен новый товар: {name}: {price}р в кол-ве {quantity}шт')
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')


def get_all_products(conn):
    """Получение всех данных с БД"""
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            conn.commit()
            result = cursor.fetchall()
            print(f'Все товары:')
            for product in result:
                print(product)
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')


def update_product_price(conn, product_id: int, new_price: int | float):
    """Обновление цены """
    try:
        with conn.cursor() as cursor:
            cursor.execute(""
                           "UPDATE products SET price = %s WHERE id = %s",
                           (product_id, new_price))
            conn.commit()
            return print(f'Цена обновлена: {new_price}')
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')


def get_product_id(conn, product_id):
    """Получение продукта по id"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, price, quantity FROM products WHERE id = %s", (product_id,))
            result = cursor.fetchone()
            if result:
                return print(f'Name: {result[0]}, price: {result[1]}, quantity: {result[2]}')
            else:
                return None
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')


def create_user(conn, name, email):
    """Добавление пользователя в БД"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                           (name, email))
            conn.commit()
            print(f'Пользователь создан: {name}: {email}')
    except psycopg2.Error as e:
        print(f'Ошибка Базы Данных: {e}')


def create_order(conn, user_id, total):
    """Создание заказа"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO orders (user_id, total) VALUES (%s, %s)",
                           (user_id, total))
            conn.commit()
            print(f'Заказ создан: user_id={user_id}, total={total}')
    except psycopg2.Error as e:
        print(f'Ошибка БД: {e}')


def get_user_orders(conn, user_id):
    """Получение заказов пользователя"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, user_id, total FROM orders WHERE user_id = %s", (user_id,))
            result = cursor.fetchall()
            if result:
                return result
            return None
    except psycopg2.Error as e:
        print(f'Ошибка БД: {e}')
        return []

def get_user_by_id(conn, user_id):
    """Возвращение информации о клиенте"""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""SELECT * FROM users
            WHERE id = %s""", (user_id, ))
            result = cursor.fetchone()
            return_dict = {'id': result[0], 'name': result[1], 'email': result[2]}
            if return_dict:
                return return_dict
            return None
    except psycopg2.Error as e:
        print(f'Ошибка БД: {e}')

def delete_order(conn, order_id):
    """Удаление заказа по id"""
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM order_items WHERE order_id = %s",
                (order_id,)
            )
            delete_order = cursor.rowcount
            cursor.execute(
                "DELETE FROM orders WHERE id = %s",
                (order_id,)
            )
            delete_string =+ cursor.rowcount
        conn.commit()
        return delete_string
    except psycopg2.Error as e:
        conn.rollback()
        print(f'Ошибка БД: {e}')
        return 0



def main():
    try:
        print(get_user_by_id(connect_to_db(), 1))
    finally:
        connect_to_db().close()


if __name__ == '__main__':
    main()
