from src.models.exceptions import NegativePriceError, InsufficientStockError


class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise NegativePriceError("Цена не может быть отрицательной")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return "Товар: " + self.name + ", Цена: " + str(self.price) + " руб., Количество: " + str(self.quantity)

    def __repr__(self):
        return "Product('" + self.name + "', " + str(self.price) + ", " + str(self.quantity) + ")"

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def sell(self, amount):
        if self.quantity < amount:
            raise InsufficientStockError(f"Товара недостаточно. На складе: {self.quantity}, требуется: {amount}")
        self.quantity = self.quantity - amount

    def apply_discount(self, discount: int) -> float:
        return self.price * (1 - discount / 100)

    def check_stock(self, req_quantity: int) -> bool:
        return self.quantity >= req_quantity

    def update_stock(self, amount: int) -> None:
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Недостаточно товара на складе")
        self.quantity = new_quantity
