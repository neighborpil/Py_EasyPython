#requests
# - urllib에서 제공하는 기능을 더 쉽고 간단하게 사용 할 수 있다

import requests

URL = 'http://www.tistory.com'
r = requests.get(URL)
print(r.text)
