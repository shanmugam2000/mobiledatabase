import sqlite3
from prettytable import prettytable
connection = sqlite3.connect("mobile.db")
table = connection.execute("select name from sqlite_master where type='table' and name='smartphones'").fetchall()
if table!=[]:
    print("Table already created.")
else:
    connection.execute('''create table smartphones(
                            name text,
                            brand text,
                            sno integer,
                            myear integer,
                            mmonth text,
                            price integer
);  ''')
    print("Table created")
while True:
    print("Select an option from the list")
    print("1.Add mobile")
    print("2.Search mobile using Serial number")
    print("3.View all mobile phones")
    print("4.update mobile phones using serial number")
    print("5.Delete mobile using serial number")
    print("6.Exit")

    choice = int(input("Enter the choice to be executed"))

    if choice ==1:
        getMname = input("Enter the mobile name:")
        getMbrand = input("Enter the mobile brand:")
        getSno = input("Enter the serial number:")
        getMyear = input("Enter the manufacturing year:")
        getMmonth = input("Enter the manufactured month:")
        getPrice = input("Enter the price of the mobile:")
        connection.execute("insert into smartphones (name,brand,sno,myear,mmonth,price) values('"+getMname+"','"+getMbrand+"',\
        "+getSno+",'"+getMmonth+"','"+getMmonth+"',"+getPrice+")")
        connection.commit()
        print("Added mobile phone successfully")

    elif choice==2:
        connection = sqlite3.connect("mobile.db")
        getSno = input("Enter the serial number of mobile to be searched:")
        result = connection.execute("select * from smartphones where sno="+getSno)
        for i in result:
            print("Mobile name",i[0])
            print("Mobile Brand",i[1])
            print("Mobile serial number",i[2])
            print("Manufactured year",i[3])
            print("Manufactured month",i[4])
            print("Price of the mobile",i[5])

    elif choice==3:
        connection = sqlite3.connect("mobile.db")
        result = connection.execute("select * from smartphones")
        table = Prettytable(["Mobile name","Mobile brand","Mobile S.no","Manu.year","Manu.month","Price"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)

    elif choice==4:
        getSno = input("Enter the serial number to be updated:")
        getMname = input("Enter the new mobile name:")
        getMbrand = input("Enter the new mobile brand:")
        getMyear = input("Enter the new manufactured year:")
        getMmonth = input("Enter the new manufactured month:")
        getPrice = input("Enter the new price:")
        connection.execute("update smartphones set name='"+getMname+"',brand='"+getMbrand+"',\
         myear='"+getMmonth+"',mmonth='"+getMmonth+"',price="+getPrice+"")
        connection.commit()
        print("updated successfully")

    elif choice==5:
        getSno = input("Enter the serial number to be updated:")
        connection.execute("delete from smartphones where sno="+getSno)
        connection.commit()
        print("Deleted successfully")

    elif choice==6:
        print("Exit")
        break

    else:
        print("Enter a valid choice")