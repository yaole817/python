import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='test')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS USER")
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
rowcount  = cursor.rowcount

print(rowcount)
conn.commit()
cursor.close()
#print('database version is %s'%data)
#conn.close()
	#print(conn)
cursor= conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
