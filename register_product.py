#Create a Diccionary for save the tuples 
registered_products = {}

# I did 3 function for call the product_id, product_name and unit_price, for the product and implement in tuples 
def product_id():
    return input("Enter Product ID: ")

def product_name():
    return input("Enter Product Name: ")   

# Place a for loop to iterate through the price unit and give the user 3 attempts to enter the price correctly.
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


#Create abbreviations for the variables: (product_id, product_name, and unit_price), so you can enter them into a Tuple.  

prod_id = product_id()
prod_name = product_name()
prod_price = unit_price()

#Here I call the variables in a Tuple.
product = (prod_id, prod_name, prod_price)

#Here call the tuples to enter them into a dict.
registered_products[prod_id] = product

print(product)