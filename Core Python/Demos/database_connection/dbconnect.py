import mysql.connector as c
#step 1
con=c.connect(
    host='localhost',
    user='root',
    password='Tiger',
    database='JulyPython'
)

if con.is_connected:
    print("Done")
else:
    print("Kuch to gadbad hai")
    
cursor=con.cursor()
# cursor.execute("Create database JulyPython")
# cursor.execute("Create table emp(eid int , ename varchar(20))")
# cursor.execute("show tables")
# for i in cursor:
#     print(i)

query="insert into emp(eid,ename) values('%s','%s')"
value=(1,"Rahul")
cursor.execute(query,value)

value=[(17,"ABD"),(18,"Virat"),(45,"Rohit")]
cursor.execute(query,value)
print(cursor.rowcount,"Affected")
con.commit()
