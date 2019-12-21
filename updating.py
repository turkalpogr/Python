
"""with open("newfile.txt","r+") as file:
    file.seek(17)
    file.write("deneme")
with open("newfile.txt", "r+") as file:
     print(file.read())"""
#************************************************************
#yukarıdaki işlmeden farklı olarak a metoduyla dökümanın sonuna ekleme yapılır

"""with open("newfile.txt","a") as file:
    file.write("siktir")

with open("newfile.txt","r") as ifile:
    print(ifile.read())
    """
    #*************************sayfa başında güncelleme
"""with open("newfile.txt", "r+") as file :
    content = file.read()
    content = "Mahmut Türkalp \n"+content
    file.seek(0)
    file.write(content)
with open("newfile.txt","r+") as ifile :
    print(ifile.read())"""
#sayfa ortasında
with open("newfile.txt","r+") as dll:
    list= dll.readlines()
    list.insert(1,"Mahmut Türkalp")
    dll.seek(0)
    dll.writelines(list)
    """ for i in list:
        dll.write(i)"""


with open("newfile.txt","r") as file :
    print(file.read())

