class Product:
    id_counter = 1

    def __init__(self, name, price, category):
        self.id = Product.id_counter
        Product.id_counter += 1
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change / 100
        else:
            self.price -= self.price * percent_change / 100

    def print_info(self):
        print(f"Product ID: {self.id}")
        print(f"Product Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:.2f}")
