#모듈 재로딩을 위한 reload 함수 찾기
try:
    from importlib import reload
except:
    try:
        from imp import reload
    except:
        pass

print('module "{}" is loaded'.format(__name__))
