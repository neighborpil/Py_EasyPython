try:
    from importlib import reload
except:
    try:
        from imp import reload
    except:
        pass


import mod_test

reload(mod_test)
