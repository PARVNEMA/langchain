import sqlite3
# * use ctrl + click to know more about as comments are written
connection =sqlite3.connect("student.db")

cursor=connection.cursor()

 ## ? create table
table_info="""
create table student(name varchar(25),class varchar (50),section varchar(25),roll_number int)
"""

cursor.execute(table_info)

cursor.execute(""" insert into student values("parv","12th","A",22)""")
cursor.execute(""" insert into student values("harsh","12th","B",23)""")
cursor.execute(""" insert into student values("himanshu","12th","C",24)""")
cursor.execute(""" insert into student values("jatav","12th","D",25)""")

data=cursor.execute(""" select * from student""")

for i in data:
    print(i)


connection.commit()
connection.close()

