import cx_Oracle

print(cx_Oracle.__file__)
con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')

# try:
#     cursor = con.cursor()
#     cursor.execute("create table Bookstore2 (name_of_book1 varchar(25), name_of_book2 varchar(25), name_of_book3 varchar(25) , price1 int, price2 int, price3 int)")
#     print("Table created successfully")
# except Exception as e:
#     print("Error1: {0}".format(e))

# try:
#     cursor2 = con.cursor()
#     cursor2.execute("insert into Bookstore2 (name_of_book1, name_of_book2 , name_of_book3, price1, price2, price3) values ('TimCook', 'JeffBezoz','Billgates', 27, 28, 29)")
#     print("Data inserted Successfully")
#     con.commit()
# except Exception as e:
#     print("Error2: {0}".format(e))

try:
    cursor3 = con.cursor()
    cursor3.execute("select * from Bookstore2")
except Exception as e:
    print("Error3: {0}".format(e))


print("writing the for loop to print the table")
for row in cursor3:
    print("printing the rows")
    print(row)


print(cursor3)


con.close()