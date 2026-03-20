Client & Order Management System

A lightweight Python CLI application for managing clients, products, and sales orders with data validation and automated reporting. 

🚀 Features
Client Management: Register clients with unique IDs, valid names (letters/spaces), and verified emails (@gmail.com, @hotmail.com).
Inventory Control: Add products with automated price validation (positive number, 3 attempts).
Order Processing: Link products to clients, auto-calculate totals, track order history. 
Financial Reports:
Total daily revenue.
Detailed final report: sales per client, product breakdown.

🛠️ Data Structure
clients_db: Dictionary storing client profiles and their order history.
registered_products: Dictionary of products using unique integer IDs as keys.

📖 Usage

Menu Options (0–6):

1.Register new client

2.Add new product

3.Create purchase order

4.View all clients and orders

5.View total revenue

6.Generate daily summary

7.Exit of the programm.

🔍 Validation Rules
IDs: Numeric and unique.
Names: Letters and spaces only.
Emails: Must end in @gmail.com or @hotmail.com, and be unique.
Prices: Positive numbers (3 input attempts allowed).

📄 Example Final Report

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

Products sold:
manzana: 5
