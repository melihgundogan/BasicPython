# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())  


#********Sayfa sonunda güncelleme

# with open("newfile.txt","a+",encoding="utf-8") as file:
#     file.write("\nKürşat")

#**********Sayfa başında güncelleme

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="Murat\n"+content 
#     file.seek(0)
#     file.write(content)
    

#**********Sayfa ortasında güncelleme    

with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"Mahmut\n")
    file.seek(0)
    file.writelines(list)
        
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())