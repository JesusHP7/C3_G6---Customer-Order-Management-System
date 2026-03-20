# Dictionary to store registered products with ID as key and (name, price) tuple as value
registered_products = {
    1234: ("manzana", 1000),
}

def unit_price():
    """Prompt the user to enter a valid unit price (positive number)."""
    for i in range(3):      
        try:
            price = float(input("Enter Unit Price: "))
            if price <= 0:
                print("Unit Price cannot be negative or zero. Please try again.")
                continue
            return price  # Return valid price
        except ValueError:
            print("Invalid input. Please enter a valid number for Unit Price.")

def add():
    """Allow user to add a new product to the registered_products dictionary."""
    p = True
    while p:
        product_id = input("\nEnter Product ID: ")
        # Validate non-empty input
        if product_id != "":
            if product_id is not None:
                # Ensure ID is numeric
                while not product_id.isdigit():
                    product_id = input("\nError, Enter Product ID: ")
                product_id = int(product_id)
                # Check for duplicate ID
                if product_id in registered_products:
                    print(f"Error: The ID '{product_id}' already exists.")
                    continue
        else:
            print("Error, please enter a Product ID.")
            continue
       
        # Get product details
        product_name = input("Enter Product Name: ").lower()
        prod_price = unit_price()

        # Confirm all values are provided before registering
        if product_name and product_id and prod_price is not None:
            product = (product_name, prod_price)
            registered_products[product_id] = product
            print("Product registered successfully!")
            p = False  # Exit loop on success
        else:
            print("Missing required input. Product not registered.")

# Call function to add a new product
add()   