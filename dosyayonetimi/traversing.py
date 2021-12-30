with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
    
    file.seek(12)
    print(file.tell())
    print(file.read())