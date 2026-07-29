# DB Connection
import pymysql

con = pymysql.connect(
    user="root",
    password="root",
    host="localhost",
    port=3306,
    db="hello_tech",
    charset="utf8mb4"
)
cur = con.cursor()

# cur.execute(""" create database saravanan_tech """)
# cur.execute(""" create table students(id int, name varchar(50), dept varchar(50), age int) """)
# cur.execute(""" insert into students values(2,"Kumar","ECE",3),(3,"Saravanan","MCA",4),(4,"Vinoth","ECE",5) """)

# name = "Mukileswar"
# dept = "CSE"
# id = 6
# age = 7
# cur.execute(""" insert into students values(%s,%s,%s,%s) """,(id,name,dept,age))

# cur.execute(""" update students set dept="IT" where id=2 """)
# cur.execute(" update students set age='5' where id=3 ")

# cur.execute(""" delete from students where id=4 """)

# cur.execute("alter table students add column phone int")
# cur.execute("alter table students drop column phone")
# cur.execute("alter table students rename column dept to department")
# cur.execute("alter table students modify column phone varchar(10)")

# Get all info from table
# cur.execute("select * from students")
# lst = cur.fetchall()
# print(lst)

# Get one user info from table
# cur.execute(""" select * from students where id=2 """)
# user = cur.fetchone()
# print(user)

# Get many user info from table
cur.execute("select * from students")
users = cur.fetchmany(2)
print(users)

con.commit()
con.close()