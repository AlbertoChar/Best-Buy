from products import Product
from store import Store


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
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)

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


if __name__ == '__main__':
    main()
