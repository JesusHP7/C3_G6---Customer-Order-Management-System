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
            return 0.0

def total_price(quantity, unit_price):
    return quantity * unit_price

if __name__ == "__main__":
    print("Product Registration")
    print("--------------------")
    continue_registration = True 

    while continue_registration:
        p_id = product_id()
        p_name = product_name()
        price = unit_price()

        print("=" * 20)
        print("\nProduct Details:")
        print(f"Product ID: {p_id}")
        print(f"Product Name: {p_name}")
        print(f"Unit Price: ${price:.2f}")

        user_input = input("Do you want to register another product? (yes/no): ").lower()
        if user_input == 'yes':
            print("\nRegistering another product...\n")
        elif user_input == 'no':
            print("Exiting product registration.")
            continue_registration = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
