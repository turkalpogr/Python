"""try :
    file = open("newfile.txt","r")
    print(file)
except FileNotFoundError as e:
    print("Dosya okunamadı"+e)
finally:
    file.close()"""
#dosya okumayı farlı şekillerde de yapabiliriz
#bunlardan biri for ile
#file = open("newfile.txt","r")

"""for i in file:
    print(i, end="")
    #veya read() metoduylada aynı işlem yapılabilir
file.close()"""
#read fonksiyonunun altında başka bir read daha yaparsak aynı dosyayaı
#boş bir içerik döner çünkü kürsör birinci okuma işleminden sonra en alt satıra gelir
#yani bir dosyayı bir defalık bir okuma işlemine tabi tutabiliriz
#content = file.read()
#print(content)
#file.close()
#readline metoduyla satır satır okuma yaptırılır
#file.readline()
#readlines metoduyla dosya içindeki her bir satır bir dizi elemanına dönüşür
#ve bu readlines metodunu bir paametreye bağlayıp onun içinden köşeli parantezler ile
#biz listeden eleman çağırır gibi satır çağrısında bulunabiliriz
"""
with open("newtext.txt","r") as file:
    contrent = file.read()
    print(content)
    metoduyle yapılan işlmelerde ayrı olarak file.close kullanmaya gerek kalmadan işlemler yapılabilir
    file.tell() fonksiyonuyla kürsorun nerede oluduğunu öğreniriz
    file.seek() metoduyla vereceğimiz bir int değerle beraber kürsör e nereye gideeceği söylenir
    
"""
