with open("sample.txt", "w+") as f:
    f.writelines("Write string s to stream.\nReturn the number of characters written\nadhflkjabdsfaksjdbakjlsdfklbasjklabjsk bhkjdfbaskhvdfkjblabfjj\n")
    f.seek(0)
    data = f.read()
    print(data)
