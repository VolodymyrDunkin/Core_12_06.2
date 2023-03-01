with open('test.txt', 'w') as fd:
    data = fd.write(' world')
    print(data)


with open('test.txt', 'a') as fd:
    data = fd.write('\nnew world')
    print(fd.tell())
    print(data)


with open('test.txt', 'w') as fd:
    data = fd.write('Hello')
    print(data)