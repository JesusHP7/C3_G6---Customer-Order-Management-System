Client & Order Management System
A lightweight Python-based Command Line Interface (CLI) application designed to manage client registrations, product inventories, and sales orders. It includes data validation and automated reporting features.

🚀 Features
Client Management: Register clients with unique IDs, name validation, and email verification (supports Gmail and Hotmail).

Inventory Control: Add new products to the system with automated price validation.

Order Processing: Link products to specific clients, calculate totals automatically, and track order history.

Financial Reports:

Calculate total daily revenue.

Generate a detailed final report showing sales per client and a breakdown of products sold.

🛠️ Data Structure
The system uses two primary dictionaries to manage data:

clients_db: Stores client profiles, including their specific order history.

registered_products: Stores available items using a unique integer ID as a key.

📖 Usage
Run the script: Execute the file using Python 3.x.

Bash
python your_script_name.py
Navigate the Menu: Use the numeric keys (0-6) to interact with the system:

1: Register a new client.

2: Add a new product to the catalog.

3: Create a purchase order for an existing client.

4: View all clients and their current orders.

5: Quick view of the total money earned.

6: Generate a comprehensive summary of the day.

🔍 Validation Rules
To ensure data integrity, the script includes the following checks:

IDs: Must be numeric and unique.

Names: Must contain only letters and spaces.

Emails: Must end in @gmail.com or @hotmail.com and must be unique.

Prices: Must be a positive number (users get 3 attempts to enter a valid price).

📄 Example Final Report
Plaintext
============================================================
FINAL DAILY REPORT
============================================================
Client ID: 001
Name: John Doe
  Order 1: manzana x5 = $5000

Total orders: 1
Total revenue: 5000

Products sold:
manzana: 5
