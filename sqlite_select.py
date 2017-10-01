import sqlite3
conn = sqlite3.connect('student.db')

sql1 = 'SELECT * FROM student WHERE no = ?'
sql2 = 'SELECT * FROM student WHERE no = :no'

c = conn.cursor()
c.execute(sql1, (2,))

print(c.fetchall())

c.execute(sql2, {"no":2}) #코드2의 딕셔너리 값으로 대
print(c.fetchall())

c.close()
