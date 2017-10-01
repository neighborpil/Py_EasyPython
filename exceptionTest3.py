#finally 처리
#파일 닫기와 같이 예외발생 여부와 상관없이 반드시 발생해야 하는 경우 사용한다
try:
    #테스트를 위하여 파일 생성

    open('__test.txt', 'w').close()

    #파일 읽기로 연다
    f = open('__test.txt', 'r')
    #파일에 먼가 쓰면 예외
    f.write('xxx')

except OSError as e:
    print('Exception : {}'.format(e))

finally:
    f.close()
    print('release file')
