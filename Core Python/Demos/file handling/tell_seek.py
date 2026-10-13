with open("abcd.txt",'a+') as f:
    print(f.tell())
    f.seek(20)
    data=f.read()
    print(data)