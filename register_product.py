registered_products = {
    1234: ("manzana", 1000),

}

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
        


def add():
  p = True
  while p:
    product_id = input("\nEnter Product ID: ")
    if product_id != "":
        if product_id is not None:
            product_id = int(product_id)
            if product_id in registered_products:
                print(f"Error: El ID '{product_id}' Already exist.")
                continue
    else:
       print("Error, enter a ")
       continue
       
    product_name = input("Enter Product Name: ").lower()
    prod_price = unit_price()

    if product_name and product_id and prod_price is not None:
        product = (product_name, prod_price)
        registered_products[product_id] = product
        print("Product registered successfully!")
        p = False
    else:
        print("Not into the value request.")

34
add()