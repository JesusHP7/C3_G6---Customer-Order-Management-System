registered_products = {}

def unit_price():
    for i in range(3):      
        try:
            price = float(input("Enter Unit Price: "))
            if price <= 0:
                print("Unit Price cannot be negative or zero. Please try again.")
                continue
            return price
        except ValueError:
            print("Invalid input. Please enter a valid number for Unit Price.")
            return None
        
p = True

while p:
    product_id = input("\nEnter Product ID: ")
    if product_id in registered_products:
        print(f"Error: El ID '{product_id}' Already exist.")
        

    product_name = input("Enter Product Name: ")
    prod_price = unit_price()

    if prod_price is not None:
        product = (product_id, product_name, prod_price)
        registered_products[product_id] = product
        print("Product registered successfully!")
    else:
        print("Could not register product due to price errors.")
    again = input("Do you want to add another product? (y/n): ").lower()
    if again != 'y':
        p = False

print("\nFinal Inventory:", registered_products)