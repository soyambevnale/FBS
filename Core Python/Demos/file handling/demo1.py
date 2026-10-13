f=None
try:
    f=open("Demos/file handling/abcde.txt","r")
    data=f.read()
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
else:
    print(data)
finally:
    if f is not None:
        print("File closed ")
        f.close()
print("Outside")