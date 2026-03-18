def register_client(clients):
    # Ask for client ID and validate that it only contains digits
    client_id = input("Enter the client ID: ")
    while not client_id.isdigit():
        print("The ID must contain only numbers.")
        client_id = input("Enter the client ID: ")

    # Check if the ID already exists in the database
    while client_id in clients:
        print("This ID is already registered, please enter another one.")
        client_id = input("Enter the client ID: ")
        while not client_id.isdigit():
            print("The ID must contain only numbers.")
            client_id = input("Enter the client ID: ")

    # Ask for client name and validate that it only contains letters (spaces allowed)
    name = input("Enter the client name: ")
    while not name.replace(" ", "").isalpha():
        print("The name can only contain letters.")
        name = input("Enter the client name: ")

    # Ask for client email and validate that it ends with @gmail.com or @hotmail.com
    email = input("Enter the client email: ")
    while not (email.endswith("@gmail.com") or email.endswith("@hotmail.com")):
        print("The email must end with @gmail.com or @hotmail.com.")
        email = input("Enter the client email: ")

    # Check if the email is already registered
    existing_emails = [data["email"] for data in clients.values()]
    while email in existing_emails:
        print("That email is already registered, please enter another one.")
        email = input("Enter the client email: ")

    # Save the client data in the dictionary
    clients[client_id] = {
        "name": name,
        "email": email
    }

    print("Client successfully registered.")
    return clients


def show_clients(clients):
    # Display all registered clients
    print("--- Client List ---")
    for client_id, data in clients.items():
        print("ID:", client_id, "| Name:", data["name"], "| Email:", data["email"])


# Initial database with one client
clients_db = {
    "1": {
        "name": "rammus",
        "email": "rammustop@gmail.com"
    }
}

# Loop to keep registering clients until user chooses to stop
continue_registering = "y"

while continue_registering == "y":
    clients_db = register_client(clients_db)
    continue_registering = input("Do you want to register another client? (y/n): ")

# Show all clients at the end
show_clients(clients_db)