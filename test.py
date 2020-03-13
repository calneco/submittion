"""
このファイルに解答コードを書いてください
"""
list1=[]
path = '/content/drive/My Drive/python_test_object-master/input.txt'

with open(path) as f:
    for line in f:
        list1.append(line.rstrip())

m = int(list1.pop())

list2=[]
for data in list1:
    a = data.split(':')
    a[0] = int(a[0])
    list2.append(a)
list2.sort()

ret=''
for data in list2:
    if m % data[0] == 0:
        ret += data[1]
if ret=='':
    print(m)
else:
    print(ret)
