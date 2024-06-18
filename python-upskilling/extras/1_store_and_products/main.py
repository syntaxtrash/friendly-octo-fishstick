from store import Store
from product import Product

store = Store("Tech Store")

# Create some Products
product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Headphones", 200, "Electronics")
product3 = Product("Coffee Maker", 80, "Home Appliances")

# Add products to the store
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Print the products info
print("Store Products:")
for product in store.products:
    product.print_info()

# Sell a product (remove by unique ID)
print("\nSelling a product:")
store.sell_product(2)

# Print the remaining products
print("\nStore Products after selling one item:")
for product in store.products:
    product.print_info()

# Apply inflation
print("\nApplying inflation:")
store.inflation(10)
for product in store.products:
    product.print_info()

# Apply discount
print("\nSetting clearance on Electronics:")
store.set_clearance("Electronics", 20)
for product in store.products:
    product.print_info()
