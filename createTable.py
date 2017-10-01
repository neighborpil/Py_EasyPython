import sqlite3
conn = sqlite3.connect('student.db')

sql = '''
    INSERT INTO student VALUES
    ("학생1", 1, "서울 간남")
'''

c = conn.cursor() #객체 생성
c.execute(sql)
c.close()
conn.commit()
