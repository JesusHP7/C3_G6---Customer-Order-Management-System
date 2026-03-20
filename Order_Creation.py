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
  
# ask quantity
  quantity = int(input("Enter quantity: "))

  product = products[product_id]

  # calculate total price
  total = product[1] * quantity

  # create order id
  order_id = len(clients[client_id]["order"]) + 1

  # save order
  clients[client_id]["order"][order_id] = {
    "product": product[0],
    "price": product[1],
    "quantity": quantity,
    "total": total
    }

  return "Order created"