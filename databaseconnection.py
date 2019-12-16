import cx_Oracle

print(cx_Oracle.__file__)
con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')

try:
    cursor = con.cursor()
    cursor.execute("create table viren2 (name varchar(25), age int)")
    print("Table create succesfully")

    cursor2 = con.cursor()
    cursor2.execute("insert into viren2 (name, age) values ('VS', 20)")
    print("Data inserted succesfully")
    con.commit()

    cursor3 = con.cursor()
    cursor3.execute("select * from viren2")

    for row in cursor3:
        print(row)

except Exception as e:
    print("We got the error: {0}".format(e))

finally:

    con.close() #conn closed
