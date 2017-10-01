import sqlite3
conn = sqlite3.connect('student.db') # connect()를 통하여 connection객체 생성
                        #student.db로 파일 생성, 없으면 생성, 있으면 기존데이터 로드
                        #":memory:"를 파일명으로 사용하면 DB를 메모리에 만든다

sql = '''
CREATE TABLE student
(
    name text,
    no integer,
    addr text
)
'''
c = conn.cursor() #객체 생성
c.execute(sql)
c.close();
