import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="LIBRARY"
)

# Creating a cursor object
cursor = connection.cursor()

# Executing the query to update BORROW Table to issue the book
cursor.execute("INSERT INTO BORROW (member_id, book_id, borrow_date) VALUES (103, 2, '2022-09-01')")

# Committing the changes
connection.commit()

# Closing the cursor and connection
cursor.close()
connection.close()
