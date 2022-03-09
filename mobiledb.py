import sqlite3
connection = sqlite3.connect("mobile.db")

listoftables = connection.execute(("SELECT name from  sqlite_master WHERE type='table' AND name='smartphones'").fetchall()

if listoftables != []:
    print("Table already exist")
else:
    connection.execute(''' create table smartphone(
                       id integer primary key autoincrement,
                       serialnum integer,
                       modelname text,
                       brand text,
                       manufactureyear integer, 
                       manufacturemonth text,
                       price integer
);   ''')

    print("table created succesfully")

    while True:
         print("select an option from menu")
         print("1. Add a smartphone ")
         print("2. View all smartphone ")
         print("3. Search a smartphone using serialno ")
         print("4. Update a samrtphone using serialno ")
         print("5. Delete a smartphone using serialno ")
         print("6. Exit ")

         choice = int(input("Enter a choice: "))

         if choice == 1:
             getSerialno = input("enter serialnum: ")
             getModelname =  input("enter modelname:")
             getBrand =  input("enter brand: ")
             getManufactureyear = input("enter manufactureyear: ")
             getManufacturemonth =
             getprice =