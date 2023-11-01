import products
from products import Product


class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self):
        products_list = []
        for product in self.products:
            if products.Product.is_active(product):
                products_list.append(product)
        return products_list

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            products.Product.buy(product, quantity)
            total += product.price * quantity
        return total
