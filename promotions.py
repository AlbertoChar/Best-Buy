from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        if self.percentage < 0 or self.percentage > 100:
            raise ValueError("Percentage discount must be between 0 and 100")
        discount = (self.percentage / 100) * product.price * quantity
        return product.price * quantity - discount


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if (quantity % 2) == 0:
            discount = (quantity / 2) * (product.price / 2)
            return (product.price * quantity) - discount
        elif quantity > 1:
            discount = (quantity - 1) / 2 * product.price / 2
            return product.price * quantity - discount
        raise ValueError("You must buy at least 2 products to get this promotion")


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            discounted_quantity = quantity - (quantity // 3)
            return discounted_quantity * product.price
        raise ValueError("You must buy at least 3 products to get this promotion")
