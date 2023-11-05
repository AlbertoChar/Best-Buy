from promotions import Promotion


class Product:
    def __init__(self, name, price, quantity, promotion = None):
        if not name:
            raise ValueError("Please enter a name for the product")
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        self.promotion = promotion

    active = True

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        if self.promotion:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity},Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity},Promotion: None"

    def buy(self, quantity):
        if not self.active:
            print("Inactive product")
            return
        if quantity <= 0:
            raise ValueError("Insert a valid quantity to purchase")
        if quantity > self.quantity and self.__class__ == NonStockedProduct.__class__:
            raise ValueError("Insufficient quantity")
        return self.promotion_handler(quantity)

    def promotion_handler(self, quantity):
        self.quantity -= quantity
        if self.promotion is None:
            return quantity * self.price
        try:
            return self.promotion.apply_promotion(self, quantity)
        except ValueError as e:
            print(f"Promotion wasn't applied: {e}")
            self.promotion = None
            return self.buy(quantity)


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        raise ValueError("Non-stocked products cannot have their quantity changed")

    def show(self):
        return f"{self.name}, Price: {self.price}"


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, max_purchase):
        super().__init__(name, price, quantity, 0)
        self.max_purchase = max_purchase

    def buy(self, quantity):
        if quantity <= self.max_purchase:
            return super().buy(quantity)
        raise ValueError(f"You can only purchase {self.max_purchase} of this product")

    def show(self):
        return f"{self.name}, Price: {self.price}, Max purchase: {self.max_purchase}"
