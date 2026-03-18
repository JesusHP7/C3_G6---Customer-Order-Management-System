registered_products = {}

def product_id():
    return input("Enter Product ID: ")

def product_name():
    return input("Enter Product Name: ")   

def unit_price():
    for i in range(3):
        try:
            price = float(input(f"Enter Unit Price: "))
            if price < 0:
                print("Unit Price cannot be negative. Please try again.")
                continue
            return price
        except ValueError:
            print("Invalid input. Please enter a valid number for Unit Price.")


prod_id = product_id()
prod_name = product_name()
prod_price = unit_price()

product = (prod_id, prod_name, prod_price)

registered_products[prod_id] = product

print("Product registered successfully!")

