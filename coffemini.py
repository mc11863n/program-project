class Coffe:
    def __init__(self,name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffe):
        self.items.append(coffe)

        print(f"Added {coffe.name} to your order.")
    
    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):

        if not self.items:
            print("Theres nothing in  this order")
            return
         
        print("\n Your order: ")

        for i, item in enumerate(self.items, 1 ):
            print(f"{i}. {item.name} - $ {item.price}")
        print(f"Total: $ {self.total()}\n")

    def checkout (self) :
        if not self.items:

            print("Your cart is empty.")

            return
        
        self.show_order()

        confirm = input("Ready for Checkout? (YES/NO): ").strip().lower()

        if confirm == "yes":
            print("Order confirmed, Thenk you.")
            self.items.clear()
        
        else:
            print("Check out is cancelled  ")


def main():

    menu = [
        Coffe("Frappuchino", 3.0),
        Coffe("Latte", 2.5),
        Coffe("Cappuccino", 3.5),
        Coffe("Americano", 2.0),
    ]

    order = Order()

    while True:

        print("\n ~ Coffe Menu ~")

        for i, coffe in enumerate(menu, 1):
            print(f"{i}. {coffe.name} - $ {coffe.price}")
        print("5. View Order")

        print("6. CheckOut")

        print("7. Exit")

        choice = input("Choose a option: ")

        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) -1])

        elif choice == '5':
            order.show_order()
        
        elif choice == '6':
            order.checkout()
        
        elif choice == '7':
            print("Thanks for coming, have a good day")

            break
        else:
            print("Invalid Choice, try again")

if __name__ == "__main__":
    main()
