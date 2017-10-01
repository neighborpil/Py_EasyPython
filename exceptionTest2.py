print('Start')

try:
    print('processing #1')
    raise Exception("Error is raised")
    print('processing #2')

except Exception:
    print('Error is handled')
else:
    print('Else state')

print('End')
