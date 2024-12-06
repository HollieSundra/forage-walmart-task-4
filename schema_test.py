import sqlite3

conn = sqlite3.connect('shipment_database.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(product);")
product_schema = cursor.fetchall()
print("Product table schema:", product_schema)

cursor.execute("PRAGMA table_info(shipment);")
shipment_schema = cursor.fetchall()
print("Shipment table schema:", shipment_schema)


conn.close()