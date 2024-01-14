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

# Executing the query to fetch all records from the BOOK Table
cursor.execute("SELECT * FROM BOOK")

# Fetching all records
records = cursor.fetchall()

# Displaying the records
for record in records:
    print(record)

# Closing the cursor and connection
cursor.close()
connection.close() 
