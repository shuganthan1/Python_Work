import pyodbc

server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

# lists inventory
inventory = cursor.execute("SELECT ProductName, QuantityPerUnit AS Quantity "
                           "FROM Products ORDER BY Quantity DESC;").fetchall()
print("Inventory:")
for product in inventory:
    print("Product name: {}\n Quantity: {}".format(product.ProductName, product.Quantity))

# lists product list
list = cursor.execute("SELECT ProductID AS ID, ProductName AS Name FROM Products ORDER BY ID;").fetchall()
print("Current Products List:")
for product in list:
    print(product.ID, product.Name)

# lists the total number of products
total = cursor.execute("SELECT COUNT(ProductID) as Total FROM Products ORDER BY Total DESC;").fetchall()
for x in total:
    y = x.Total
print("The company sells {} products".format(y))

# lists the total orders for each product - only displays products that have orders
orders = cursor.execute("SELECT ProductName, SUM(UnitsOnOrder) AS 'Total' FROM Products GROUP BY ProductName HAVING SUM(UnitsOnOrder) > 0 ORDER BY 'Total' DESC;").fetchall()
for x in orders:
    print(x.ProductName, x.Total)

# lists current products less than £20
rows = cursor.execute("SELECT ProductID, ProductName, UnitPrice FROM Products WHERE UnitPrice < 20 ORDER BY UnitPrice DESC;").fetchall()
print("Products under £20:")
for product in rows:
    print("ID: {} Product: {}\n Price: £{}".format(product.ProductID, product.ProductName, product.UnitPrice))
