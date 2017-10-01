def func1():
    raise Exception("error is raise")

def func2():
    func1()


func2() # 예외가 발생시 호출 경로를 담고 있는 프레임 정보를 가지고 있는 trackback
        # 객체를 예외 클래스에 담아 예외 발생 위치를 좀 더 잘 보여준다
