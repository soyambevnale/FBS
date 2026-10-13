import mysql.connector as ct
# con=None
# try:
con=ct.connect(
        host='localhost',
        user='root',
        password='Tiger',
        use_pure=True,
        database='Soyam'
    )

cur=con.cursor()
    # cur.execute("Create database  Soyam")
    # print("ABC database created successfully!")

    # cur.execute("create table  student_ty(roll_no int,name varchar(40))")
    # cur.execute("show student_FY")
    # cur.execute("show databases")
    # for i in cur:
    #     print(i)
    # cur.execute("insert into student_FY(name,roll_no)values(%s,%s),('Rohit',12)")
    # query="insert into student_ty(name,roll_no)values(%s,%s)"
    # values=[("Virat",12),("Rohit",18)]
    # cur.executemany(query,values)
    # print(cur.rowcount,"affected")
    # con.commit()
# cur.execute("select * from Student_ty")
    # d=cur.fetchone()
    # print(d)
# d=cur.fetchall()
    # print(d)
# for i in d:
#     print(i)
    # q="update student_ty set name=%s where roll_no=%s"
    # val=("Virat Kolhi",12)
    # # cur.execute(q,val)
    # val=[("Virat Kolhi",12),("Smriti",45)]
    # cur.executemany(q,val)
    # print(cur.rowcount,"is affected")

    # con.commit()
    # d=cur.fetchall()
# except Exception as e:
#     print(e)


# qd="delete from student_ty where roll_no=%s"
# val=(18,)
# cur.execute(qd,val)
# con.commit()
# print(f"{cur.rowcount} Rows affected")

tq="truncate table student_ty"
cur.execute(tq)
con.close()

# if con is not None:
#     print("Connection is done")
# else:
#     print("Kuch to gadbad hai")
