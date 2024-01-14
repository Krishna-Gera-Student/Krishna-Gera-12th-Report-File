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

# Executing the query to fetch records from the MEMBER Table
cursor.execute("SELECT * FROM MEMBER WHERE member_id % 2 = 1 AND name LIKE 'J%'")

# Fetching records
records = cursor.fetchall()

# Displaying the records
for record in records:
    print(record)

# Closing the cursor and connection
cursor.close()
connection.close() 
