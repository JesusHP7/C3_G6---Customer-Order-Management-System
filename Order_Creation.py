def agg_order(clients, products):
  # ask client id
  client_id = input("Enter client ID: ")

  if client_id not in clients:
    return "Client not found"

# ask product id
  product_id = input("Enter product ID: ")
  while not product_id.isdigit():
    product_id = input("Enter product ID: ")

  product_id = int(product_id)

  if product_id not in products:
    return "Product not found"