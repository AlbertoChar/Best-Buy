class Product:
    def __init__(self, name, price, quantity):

        if not name:
            raise ValueError("Please enter a name for the product")
        else:
            self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.price = price
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        else:
            self.quantity = quantity

    active = True

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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if self.active:
            if quantity <= 0:
                raise ValueError("Insert a valid quantity to purchase")
            elif quantity > self.quantity:
                raise ValueError("Insufficient quantity")
            else:
                self.quantity -= quantity
                return quantity * self.price
