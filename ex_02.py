# with open('data.bin', 'wb') as fd:
#     fd.write("Привіт світ".encode('CP1251'))


# with open('data.bin', 'rb') as fd:
#     data = fd.read()
#     print(data.decode('CP1251'))


# with open('data.bin', 'wb') as fd:
#     fd.write("Привіт з України".encode())

with open('data.bin', 'rb') as fd:
    data = fd.read()
    print(data.decode())