
# File I/O

with open("demo.txt",'a+') as f:
    f.seek(0)
    data = f.read()
    print(data)

    f.write("appended the single line into the demo file\n")
    
    print(f.read())



