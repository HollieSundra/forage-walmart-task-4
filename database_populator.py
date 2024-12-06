import sqlite3
import csv

def insert_products():
    # Read products from the CSV file
    with open('data/shipping_data_0.csv', 'r') as file:
        reader = csv.DictReader(file)
        products = set(row['product'] for row in reader)  # Use a set to avoid duplicates
    
    # Establish connection to the SQLite database
    conn = sqlite3.connect('shipment_database.db')
    cursor = conn.cursor()

    # Loop through products and insert them if they don't exist
    for product in products:
        cursor.execute('SELECT id FROM product WHERE name = ?', (product,))
        existing_product = cursor.fetchone()

        if existing_product:
            print(f"Product already exists: {product}")
            continue

        # Insert product if it doesn't exist
        cursor.execute('''
            INSERT INTO product (name)
            VALUES (?)
        ''', (product,))
        print(f"Inserted product: {product}")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_shipments():
    # Open the CSV file and read the data
    with open('data/shipping_data_0.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Fetch product_id based on product name
            cursor.execute('''
                SELECT id FROM product WHERE name = ?
            ''', (row['product'],))
            product_id = cursor.fetchone()

            if product_id is None:
                print(f"Product not found: {row['product']}")
                continue

            product_id = product_id[0]

            # Insert shipment data
            cursor.execute('''
                INSERT INTO shipment (product_id, quantity, origin, destination)
                VALUES (?, ?, ?, ?)
            ''', (product_id, int(row['product_quantity']), row['origin_warehouse'], row['destination_store']))
        
def main():
    # Establish connection to the SQLite database
    conn = sqlite3.connect('shipment_database.db')
    global cursor
    cursor = conn.cursor()

    # Insert products and shipments
    insert_products()
    insert_shipments()

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
