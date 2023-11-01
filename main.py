from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def start(store):
    print("Welcome to the store")
    print("Select an option:")
    print("1. List all products in store")
    print("2. Show the total amount in store")
    print("3. Make an order")
    print("4. Quit")
    choice = input()
    return int(choice)


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, max_purchase=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", 30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = Store(product_list)
    while True:
        choice = start(best_buy)
        if choice == 1:
            all_products = best_buy.get_all_products()
            for product in all_products:
                print(product.show())
        elif choice == 2:
            total_quantity = best_buy.get_total_quantity()
            print(total_quantity)
        elif choice == 3:
            print("Which product would you want to buy? (number of the product)")
            product_num = int(input())
            print("How many?")
            product_quantity = int(input())
            shopping_list = [(product_list[product_num], product_quantity)]
            total_cost = best_buy.order(shopping_list)
            print(f"Total cost of the order: ${total_cost}")
        elif choice == 4:
            print("Goodbye!")
            break  # Exit the loop and end the program


if __name__ == '__main__':
    main()
