import sqlite3

conn = sqlite3.connect('Data/company_product_db.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT * FROM products WHERE company_id=396")  # table name, not database name
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()