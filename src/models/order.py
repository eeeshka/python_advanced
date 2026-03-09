from src.models.exceptions import InvalidOrderError

class Order:
    def __init__(self, user, products, order_id=None):
        if not products or len(products) == 0:
            raise InvalidOrderError("Заказ невалиден: пустой список товаров")
        self.user = user
        self.products = products
        self.order_id = order_id
        self.total = self.calculate_total()
    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total = total + product.get_total_price()
        return total
    
    def __str__(self):
        if self.order_id:
            user_name = self.user.name if hasattr(self.user, 'name') else str(self.user)
            return "Заказ #" + str(self.order_id) + " на сумму " + str(self.total) + " руб. (Пользователь: " + user_name + ")"
        else:
            user_name = self.user.name if hasattr(self.user, 'name') else str(self.user)
            return "Заказ на сумму " + str(self.total) + " руб. (Пользователь: " + user_name + ")"