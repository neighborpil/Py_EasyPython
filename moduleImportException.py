#import시 예외처리
try:
    import unknown_module
except ImportError:
    print("unknown_module is not loaded")

try: #1. webob와 restkit모듈을 로드
    import webob 
    import restkit
except ImportError: #2. 문제시 PyQuery 임포트
    from.pyQuery import PyQuery
else: #3. import에 문제가 없으면 PyQuery심볼을 만든다
    from.ajax import PyQuery
