#urllib
# - 파이썬 표준 모듈
# - 특정 웹페이지의 html코드를 볼 수 있다

from urllib.request import urlopen
html = urlopen('http://en.wikipedia.org/wiki/Main_Page')
doc = html.read().decode('utf-8') #byte타입을 str타입로 디코딩
print(doc)
