import pymysql

conn=pymysql.connect(host="localhost",user="root",passwd="",db="pythonexample")

myCursor=conn.cursor()
myCursor.execute("select id,name from student")
#print(myCursor.fetchall(), end="\n")

all_rows = myCursor.fetchall()
print(type(all_rows))
print (len(all_rows))


for row in all_rows:
    print (row['id'])
    print (row['name'])

conn.commit()
conn.close()


'''
CREATE TABLE student (
    id int,
    name varchar(255)
);
INSERT INTO student(id,name) VALUES (1,'shaiful'),(2,'ferdous');
'''