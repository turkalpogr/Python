mylist = [1,2,3]
print(len(mylist))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Film objesi oluşturuldu")
    #java daki oviride string metodu mantığıyla çalışır 
    def __str__(self):
        return f"{self.title} by {self.director}"
    #bu classın içine len metodunu eklemeden herhangi bir şekilde
    #class a uzunluk değeri sorgulaması yollayamazsın
    def __len__(self):
        return self.duration
m=Movie("Film adı","yönetmen",123)
print(str(m))
print(len(m))