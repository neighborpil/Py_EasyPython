import sqlite3
conn = sqlite3.connect('student.db')

sql = 'SELECT * FROM student'

c = conn.cursor()
c.execute(sql)

#하나의 데이터만
print(c.fetchone())

print()
#10개의 데이터를
for s in c.fetchmany(3):
    print(s)
print()
#모든 데이터를 가져온다
for s in c.fetchall():
    print(s)

c.close()
