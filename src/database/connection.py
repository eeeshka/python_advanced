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
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
                       (name, price, quantity))
        conn.commit()
        return print(f'Добавлен новый товар: {name}: {price}р в кол-ве {quantity}шт')


def get_all_products(conn):
    """Получение всех данных с БД"""
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM products')
        conn.commit()
        result = cursor.fetchall()
        print(f'Все товары:')
        for product in result:
            print(product)


def update_product_price(conn, product_id: int, new_price: int | float):
    """Обновление цены """
    with conn.cursor() as cursor:
        cursor.execute(""
                       "UPDATE products SET price = %s WHERE id = %s",
                       (product_id, new_price))
        conn.commit()
        return print(f'Цена обновлена: {new_price}')


def get_product_id(conn, product_id):
    """Получение продукта по id"""
    with conn.cursor() as cursor:
        cursor.execute("SELECT name, price, quantity FROM products WHERE id = %s", (product_id,))
        result = cursor.fetchone()
        if result:
            return print(f'Name: {result[0]}, price: {result[1]}, quantity: {result[2]}')
        else:
            return None

def main():
    add_product(connect_to_db(), 'Ноутбук', 50000, 10)
    add_product(connect_to_db(), 'Мышь', 1500, 20)
    add_product(connect_to_db(), 'Монитор', 12000, 10)
    get_all_products(connect_to_db())
    update_product_price(connect_to_db(), 1, 45000)


if __name__ == '__main__':
    main()