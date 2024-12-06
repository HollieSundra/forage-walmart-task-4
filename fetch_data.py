import sqlite3

def fetch_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('shipment_database.db')
    cursor = conn.cursor()

    # Fetch and display all data from the product table
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    print("Products:")
    for product in products:
        print(product)

    # Fetch and display all data from the shipment table
    cursor.execute("SELECT * FROM shipment")
    shipments = cursor.fetchall()
    print("\nShipments:")
    for shipment in shipments:
        print(shipment)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    fetch_data()
