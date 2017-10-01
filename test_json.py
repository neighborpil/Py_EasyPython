import json

person1 = {
    'name' : '김하나',
    'height' : 170,
    'weight' : 60
}

print(json.dumps(person1)) #json.dumps() : 바이트 문자열로 변환, 그대로 파일 저장 가능 or 바로 사용도 가능

#with open('test.json', 'w') as f:
#    json.dump(person1, f)
