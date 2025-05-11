class Product:
    """
    Product Inventory Menu:
    1. Add new product
    2. Delete a product
    3. Calculate total value
    4. Display product info
    5. Exit
    """

    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self, product_id):
        print("\n--- Product Info ---")
        print(f"Product ID : {product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ${self.price}")
        print(f"Quantity   : {self.quantity}")
        print(f"Total Value: ${self.total_value()}")


# ===== MAIN PROGRAM =====
products = {}  # product_id -> Product instance
product_counter = 1  # Start with product ID 1

while True:
    print("\n" + "-" * 40)
    print(Product.__doc__)  # Show menu from docstring
    print("-" * 40)

    choice = input("Choose an option (1-5): ")

    try:
        if choice == "1":
            # Auto-generate the product ID
            product_id = f"p{product_counter}"
            product_counter += 1  # Increment the counter for the next product ID

            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            products[product_id] = Product(name, price, quantity)
            print(f"Product added successfully with ID {product_id}.")

        elif choice == "2":
            if not products:
                print("No products available to delete.")
                continue
            product_id = input("Enter product ID to delete: ")
            if product_id in products:
                del products[product_id]
                print(f"Product with ID {product_id} deleted successfully.")
            else:
                print("Product ID not found.")

        elif choice == "3":
            if not products:
                print("No products available. Please add one first.")
                continue
            product_id = input("Enter product ID: ")
            if product_id in products:
                product = products[product_id]
                print(f"Total value of {product.name}: ${product.total_value()}")
            else:
                print("Product ID not found.")

        elif choice == "4":
            if not products:
                print("No products available. Please add one first.")
                continue
            product_id = input("Enter product ID: ")
            if product_id in products:
                product = products[product_id]
                product.display_info(product_id)
            else:
                print("Product ID not found.")

        elif choice == "5":
            print("Exiting. Thank you.")
            break

        else:
            print("Please choose a valid option (1–5).")

    except ValueError as e:
        print("Input error:", e)