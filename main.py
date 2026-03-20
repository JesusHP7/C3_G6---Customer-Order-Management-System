# -------------------------------
# Bases de datos iniciales
# -------------------------------
clients_db = {
    "001": {"name": "Luis", "email": "luis@gmail.com"},
    "002": {"name": "Ana", "email": "ana@hotmail.com"},
    "003": {"name": "Carlos", "email": "carlos@gmail.com"}
}

registered_products = {
    1234: ("manzana", 1000),
    5678: ("pera", 1500),
    9101: ("uva", 2000)
}

orders_db = {}      

# -------------------------------
# Funciones
# -------------------------------
def register_client(client_id, name, email):
    if client_id in clients_db:
        return f"Error: Client ID {client_id} already exists."
    if not client_id.isdigit():
        return "Error: Client ID must be numeric."
    if not name.replace(" ", "").isalpha():
        return "Error: Name must contain only letters."
    if not (email.endswith("@gmail.com") or email.endswith("@hotmail.com")):
        return "Error: Email must end with @gmail.com or @hotmail.com"

    clients_db[client_id] = {"name": name, "email": email}
    return f"Client {name} registered successfully!"


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


def register_product():
    p = True
    while p:
        product_id = input("\nEnter Product ID: ")
        if not product_id.isdigit():
            print("Error: Product ID must be numeric.")
            continue
        product_id = int(product_id)

        if product_id in registered_products:
            print(f"Error: El ID '{product_id}' Already exist.")
            continue

        product_name = input("Enter Product Name: ").lower()
        prod_price = unit_price()

        if prod_price is not None:
            registered_products[product_id] = (product_name, prod_price)
            print("Product registered successfully!")
        else:
            print("Could not register product due to price errors.")

        again = input("Do you want to add another product? (y/n): ").lower()
        if again != 'y':
            p = False


def create_order(order_id, client_id, product_id, quantity):
    if order_id in orders_db:
        return f"Error: Order ID {order_id} already exists."
    if client_id not in clients_db:
        return "Error: Client not found."
    if product_id not in registered_products:
        return "Error: Product not found."
    if quantity <= 0:
        return "Error: Quantity must be greater than zero."

    product_name, unit_price = registered_products[product_id]
    total = unit_price * quantity

    orders_db[order_id] = {
        "client": clients_db[client_id]["name"],
        "product": product_name,
        "quantity": quantity,
        "total": total
    }
    return f"Order {order_id} created successfully! Total: {total}"


def view_orders():
    if not orders_db:
        return "No hay pedidos registrados."
    
    print("\n--- Pedidos Registrados ---")
    print(f"{'Order ID':<10} {'Cliente':<15} {'Producto':<15} {'Cantidad':<10} {'Total':<10}")
    print("-" * 60)
    for order_id, order in orders_db.items():
        print(f"{order_id:<10} {order['client']:<15} {order['product']:<15} {order['quantity']:<10} {order['total']:<10}")
    return "Consulta finalizada."


def calculate_daily_income():
    if not orders_db:
        return "No hay pedidos registrados."
    total_income = sum(order["total"] for order in orders_db.values())
    return f"Ingresos del día: {total_income}"


def generate_final_report():
    if not orders_db:
        return "No hay pedidos registrados."
    
    total_orders = len(orders_db)
    total_income = sum(order["total"] for order in orders_db.values())
    
    report_by_client = {}
    for order in orders_db.values():
        client = order["client"]
        if client not in report_by_client:
            report_by_client[client] = []
        report_by_client[client].append(order)
    
    print("\n--- Reporte Final ---")
    print(f"Total de pedidos: {total_orders}")
    print(f"Ingresos del día: {total_income}")
    print("\nPedidos por cliente:")
    for client, orders in report_by_client.items():
        print(f"- {client}:")
        for o in orders:
            print(f"   Producto: {o['product']}, Cantidad: {o['quantity']}, Total: {o['total']}")
    return "Reporte generado."


# -------------------------------
# Menú principal
# -------------------------------
choice = ""
while choice != "0":
    print("\n--- MENÚ ---")
    print("1 → Register client")
    print("2 → Register product")
    print("3 → Create order")
    print("4 → View orders") 
    print("5 → Calculate daily income")
    print("6 → Generate final report")
    print("0 → Exit")
    choice = input("Please enter the option: ")

    if choice == "1":
        cid = input("Client ID: ")
        name = input("Name: ")
        email = input("Email: ")
        print(register_client(cid, name, email))

    elif choice == "2":
        register_product()

    elif choice == "3":
        oid = input("Order ID: ")
        cid = input("Client ID: ")
        pid = int(input("Product ID: "))
        qty = int(input("Quantity: "))
        print(create_order(oid, cid, pid, qty))

    elif choice == "4":
        print(view_orders())

    elif choice == "5":
        print(calculate_daily_income())

    elif choice == "6":
        print(generate_final_report())

    elif choice == "0":
        print("Exiting system...")

    else:
        print("Invalid option")