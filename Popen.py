#Popen
# - 외부 프로그램과 데이터 교환 위해 사용

import subprocess

cmd = ['ping', '-t', '10', 'www.google.com']
output = subprocess.check_output(cmd)
print(output)
