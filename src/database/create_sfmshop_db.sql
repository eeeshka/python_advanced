create TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

create TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER DEFAULT 0
);

create TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2),
    create_at TIMESTAMP DEFAULT NOW()
);

create TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    price DECIMAL(10, 2) NOT NULL
);


insert into users (name, email) values
    ('Влад', 'nnbull2602@gmail.com'),
    ('Регина', 'regavonadgob@mail.ru'),
    ('Наталья', 'zurka1997@mail.ru');


INSERT INTO products (name, price, quantity) values
    ('Ноутбук', 199000, 10),
    ('iPhone 17 pro', 124000, 10),
    ('Телевизор 50', 74000, 10),
    ('Холодильник', 55000, 10),
    ('Стиральная машина', 34999, 10);

INSERT INTO orders (user_id, total) values
    (1, 50000),
    (2, 75000);

INSERT INTO order_items (order_id, product_id, quantity, price) values
    (1, 1, 1, 50000),
    (2, 2, 1, 34000),
    (2, 3, 1, 34000);


SELECT * FROM order_items