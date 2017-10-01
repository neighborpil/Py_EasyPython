#테스트 모듈

#파일명: my_math.py
"""
My Math
=======
"""

__all__ = ['fib'] #특별, 외부로 노출하고 싶은 것들을 문자열로 정의
                  #from my_math import *와 같이 로드하면 __all__에서 정의한 심볼만 로드
#모듈 버전
__version__ = 1.0

#원주율
PI = 3.1415

def fib(n):
    "피보나치 수열 생성"
    a, b = 0, 1

    while b < n:
        yield b
        a, b = b, a + b
