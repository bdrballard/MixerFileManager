# Example code for connecting to a MySQL database in python
# Note you should first create the database on your server.
# This database for constructed using the MySQL Workbench software.
# You need to first install MySQL and then MySQL Workbench.
import globals
import csv  # for handling comma separated variable data

import mysql
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host ='localhost',
                                          database = 'Electronics',
                                          user= 'root',
                                          password = 'password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database...MySQL version on ", db_Info)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if not connection.is_connected():
        pass
    else:
        connection.close()
        print("MySQL connection is closed")

# Example of Creating a MySQL table from Python
# The following import is commented out if you choose not to
# make this a def function
# import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='password')
    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS Laptop (
                                id int(11) NOT NULL,
                                Name varchar(250) NOT NULL,
                                Price float NOT NULL,
                                Purchase_date Date NOT NULL,
                                PRIMARY KEY (Id))"""

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as Error:
    print ("Failed to create table in MySQL:{}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# example code for reading a file containing csv data and inserting it into a database

# to do  put the following in a try catch block

connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='password')

cursor = connection.cursor()
csv_data = csv.reader(open('/Users/danballard/Desktop/Laptop_inventory.csv'))
header = next(csv_data)

print("Importing the CSV File ")
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO Laptop(id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)", row)
connection.commit()
cursor.close()
print ("Done")

