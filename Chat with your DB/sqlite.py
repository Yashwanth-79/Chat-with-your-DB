import sqlite3


connection = sqlite3.connect("nammastore.db")


cursor = connection.cursor()


cursor.execute("""
CREATE TABLE Category (
    CategoryID INTEGER PRIMARY KEY,
    CategoryName VARCHAR(30)
)
""")

cursor.execute("""
CREATE TABLE Supplier (
    SupplierID INTEGER PRIMARY KEY,
    SName VARCHAR(30),
    Address VARCHAR(50),
    Phone VARCHAR(15)
)
""")

cursor.execute("""
CREATE TABLE Customer (
    CustomerID VARCHAR(30) PRIMARY KEY,
    Name VARCHAR(30),
    Address VARCHAR(50),
    Phone VARCHAR(15),
    Password VARCHAR(15)
)
""")

cursor.execute("""
CREATE TABLE Product (
    ProductID INTEGER PRIMARY KEY,
    Pname VARCHAR(30),
    CategoryID INTEGER,
    SupplierID INTEGER,
    Quantity_in_stock INTEGER,
    UnitPrice INTEGER,
    ReorderLevel INTEGER,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
)
""")

cursor.execute("""
CREATE TABLE Transaction_Information (
    TransactionID INTEGER PRIMARY KEY,
    CustomerID VARCHAR(30),
    Trans_Init_Date DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
)
""")

cursor.execute("""
CREATE TABLE Transaction_Detail (
    TransactionID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    Discount INTEGER DEFAULT 0,
    Total_Amount INTEGER,
    Trans_Init_Date DATE,
    PRIMARY KEY (TransactionID, ProductID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Information(TransactionID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
)
""")

cursor.execute("""
CREATE TABLE Payment (
    TransactionID INTEGER PRIMARY KEY,
    Amount_Paid INTEGER,
    Mode VARCHAR(30),
    Transaction_Date DATE,
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Information(TransactionID)
)
""")

cursor.execute("""
CREATE TABLE Price_List (
    ProductID INTEGER PRIMARY KEY,
    USP INTEGER,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
)
""")

cursor.execute("""
CREATE TABLE Depleted_Product (
    ProductID INTEGER PRIMARY KEY,
    Quantity INTEGER,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
)
""")

# Insert data into tables
cursor.executemany("INSERT INTO Category VALUES (?,?)", [
    (1, 'Food'), (2, 'Cosmetics'), (3, 'Personal Hygiene'), (4, 'Pets'),
    (5, 'Electronics'), (6, 'Clothing'), (7, 'Books'), (8, 'Home & Garden'),
    (9, 'Sports'), (10, 'Toys')
])

cursor.executemany("INSERT INTO Supplier VALUES (?,?,?,?)", [
    (2, 'Arham', 'Saddar', '03011567430'),
    (6, 'Lohit', 'Gulshan', '03318746556'),
    (8, 'Sarim', 'Malir', '03231264454'),
    (12, 'Farzan', 'Layari', '03003325459'),
    (15, 'Ali Traders', 'Orangi', '03331234567'),
    (18, 'Tech Solutions', 'DHA', '03219876543'),
    (21, 'Green Leaf', 'Korangi', '03001122334'),
    (24, 'Fashion Hub', 'Tariq Road', '03452233445'),
    (27, 'Book World', 'Clifton', '03123456789'),
    (30, 'Sports Gear', 'PECHS', '03214567890')
])

cursor.executemany("INSERT INTO Customer VALUES (?,?,?,?,?)", [
    ('A1', 'Usman Yaqoob', 'Gulshan', '03231234509', 'abc12'),
    ('A2', 'Manahil Fatima', 'Johar', '03351356204', 'mypassword'),
    ('A3', 'Anas Ahmed', 'DHA', '03247894651', 'whocares'),
    ('A4', 'Sara Ali', 'Clifton', '03331234567', 'pass123'),
    ('A5', 'Ahmed Khan', 'PECHS', '03219876543', 'securepass'),
    ('A6', 'Fatima Hassan', 'Nazimabad', '03001234567', 'fatima123'),
    ('A7', 'Ali Raza', 'North Nazimabad', '03331122334', 'alipass'),
    ('A8', 'Zainab Malik', 'Defence', '03002233445', 'zainab789'),
    ('A9', 'Omar Farooq', 'Bahadurabad', '03123456789', 'omarpass'),
    ('A10', 'Ayesha Imran', 'Gulistan-e-Johar', '03214567890', 'ayesha456')
])

cursor.executemany("INSERT INTO Product VALUES (?,?,?,?,?,?,?)", [
    (1, 'KnS Qeema Extra Lean', 1, 12, 150, 480, 50),
    (2, 'Pringles Salted', 1, 12, 55, 100, 30),
    (3, 'Blue for Women Deodorant', 2, 2, 20, 300, 20),
    (4, 'Maybelline Sky High Mascara', 3, 6, 30, 680, 10),
    (5, 'Fluffy Cat Food', 4, 8, 102, 500, 20),
    (6, 'Smartphone X', 5, 2, 80, 1000, 15),
    (7, 'Cotton T-Shirt', 6, 6, 200, 250, 50),
    (8, 'Bestseller Novel', 7, 8, 50, 350, 20),
    (9, 'Garden Tools Set', 8, 12, 25, 800, 10),
    (10, 'Tennis Racket', 9, 2, 40, 600, 15)
])

cursor.executemany("INSERT INTO Transaction_Information VALUES (?,?,?)", [
    (16, 'A1', '2022-12-04'), (23, 'A2', '2022-12-03'),
    (27, 'A2', '2022-12-03'), (28, 'A3', '2022-12-01'),
    (29, 'A4', '2022-12-05'), (30, 'A5', '2022-12-06'),
    (31, 'A6', '2022-12-07'), (32, 'A7', '2022-12-08'),
    (33, 'A8', '2022-12-09'), (34, 'A9', '2022-12-10')
])

cursor.executemany("INSERT INTO Transaction_Detail VALUES (?,?,?,?,?,?)", [
    (16, 4, 2, 0, 960, '2022-12-01'), (16, 5, 5, 0, 2500, '2022-12-01'),
    (23, 1, 5, 0, 2400, '2022-12-03'), (23, 2, 10, 0, 1000, '2022-12-03'),
    (27, 1, 15, 0, 7200, '2022-12-04'), (27, 2, 30, 0, 3000, '2022-12-04'),
    (27, 3, 12, 0, 3600, '2022-12-04'), (28, 5, 10, 0, 5000, '2022-12-04'),
    (29, 6, 2, 0, 2000, '2022-12-05'), (30, 7, 5, 0, 1250, '2022-12-06')
])

cursor.executemany("INSERT INTO Payment VALUES (?,?,?,?)", [
    (16, 3400, 'credit card', '2022-12-01'), (23, 5440, 'cash', '2022-12-03'),
    (27, 1560, 'debit card', '2022-12-04'), (28, 5254, 'debit card', '2022-12-04'),
    (29, 2000, 'credit card', '2022-12-05'), (30, 1250, 'cash', '2022-12-06'),
    (31, 3600, 'credit card', '2022-12-07'), (32, 1000, 'debit card', '2022-12-08'),
    (33, 2500, 'cash', '2022-12-09'), (34, 1800, 'credit card', '2022-12-10')
])

cursor.executemany("INSERT INTO Price_List VALUES (?,?)", [
    (1, 230), (2, 100), (3, 560), (4, 40), (5, 30),
    (6, 1000), (7, 250), (8, 350), (9, 800), (10, 600)
])

cursor.executemany("INSERT INTO Depleted_Product VALUES (?,?)", [
    (3, 5), (4, 8), (6, 10), (8, 15), (9, 7),
    (10, 12), (1, 20), (2, 25), (5, 18), (7, 30)
])


connection.commit()


tables = ['Category', 'Supplier', 'Customer', 'Product', 'Transaction_Information', 
          'Transaction_Detail', 'Payment', 'Price_List', 'Depleted_Product']

for table in tables:
    print(f"\nRecords from {table} table:")
    data = cursor.execute(f"SELECT * FROM {table}")
    for row in data:
        print(row)

connection.close()
