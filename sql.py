#readme file - basic requirement of the project for someone else to read
#touch  readme.md to create on gitbash
#pyodbc is an open source Python module that makes accessing ODBC databases simple
#that allows applications to access data in database management systems(DBMS)
#using SQL as a standard for accessing the data
#pyodbc is an implementation of a driver that allows you to connect to any database
#link beterrnpython and any database management systems

import pyodbc
#connecting to northwind database
server = 'localhost,1433'
database = 'Northwind'
username ='SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)
#a cursor itself is a control structure
#that allows us to control and manage rows of data from a response
cursor = docker_Northwind.cursor()
#object cursor and then referencing
cursor.execute('SELECT @@version;')
row = cursor.fetchone()
print('The row is',row)

cust_rows = cursor.execute('SELECT * FROM Customers;').fetchone()
print('Customer rows are', cust_rows)

rows = cursor.execute('SELECT * FROM Products').fetchall()
#print ('Unit price')
for record in rows:
    print(record.UnitPrice)
#list lastname for all employees from employee table
rows1= cursor.execute('SELECT LastName FROM Employees').fetchall()
print(rows1)
rows2 = cursor.execute('SELECT LastName FROM Employees').fetchall()
print(rows2)
#list names of employees who live either in london or seattle
rows = cursor.execute('SELECT *FROM Employee WHERE CITY = London OR City = Seattle').fetchall()
print('Full Name')
for record in rows:
    print(record.FirstName,record.LastName)