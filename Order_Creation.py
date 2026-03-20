def agg_order(clients, products):
  # ask client id
  client_id = input("Enter client ID: ")

  if client_id not in clients:
    return "Client not found"

