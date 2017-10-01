#Random.py
# 코드 일부분인데 테스트 위해 사용
class Random(_random.Random):
    #생략...

    def seed(self, a = None, version = 2):
        #생략...
        if version == 2:
            if isinstance(a, (str, bytes, bytearray)): # a 객체가 str, bytes, bytearray 중 하나의 타입인지 확인
                if isinstance(a, str):
                    a = a.encode()
                a += sha512(a).digest()
                a = int.from_bytes(a, 'big')
