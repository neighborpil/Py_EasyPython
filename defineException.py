#유저정의 예외1
class OwnerError(Exception): # 상속
    def __init__(self, message):
        self.message = message

#유저 정의 예외2
class MyError(Exception): pass #예외 클래스 자체가 예외를 설명하기 때문에 이와
                               #같이 클래스만 정의해도 된

try:
    raise OwnerError(" 조용")
except OwnerError as e:
    print("사장: ", e.message)

try:
    raise MyError
except MyError as e:
    print(e.message)
