import sys
# sys.argv
ars = sys.argv
print('引數:')
for ind, ar in enumerate(ars):
    print('sys.argv[%d]: %s' % (ind, ar))
print('引數至少一個就是程式名稱')
# sys.path
print('import 模組搜尋路徑:')
for ind, path in enumerate(sys.path):
    print(ind, ':', path)
# sys.version
print('版本:')
print('sys.version:', sys.version)
# sys.getsizeof()
print('sys.getsizeof(x)')
print('int:  ', sys.getsizeof(1), 'Bytes')
print('float:', sys.getsizeof(1.), 'Bytes')
print('str:  ', sys.getsizeof('S'), 'Bytes')
print('tuple:', sys.getsizeof(()), 'Bytes')
print('list: ', sys.getsizeof([]), 'Bytes')
print('dict: ', sys.getsizeof({}), 'Bytes')
print('set:  ', sys.getsizeof(set()), 'Bytes')
print('bytes: ', sys.getsizeof(b''), 'Bytes')
print('bytearray:', sys.getsizeof(bytearray([])), 'Bytes')
