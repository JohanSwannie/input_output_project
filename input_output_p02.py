with open('binary_file1.txt', 'rb') as bf:
    data = bf.read()
    print(data)

with open('binary_file1.txt', 'r') as binf:
    data2 = binf.read(8)
    while data2 != '':
        text = chr(int(data2, 2))
        print(text, end = '')
        data2 = binf.read(8)
