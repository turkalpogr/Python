import  json
import os
class User:
    def __init__(self, username, passw, email):
        self.username = username
        self.passw = passw
        self.email = email

class UserRepo:
    def __init__(self):
        self.users = []
        self.isLogged =False
        self.currentUser = {}

        self.loadUsers()
    def loadUsers(self):
        if os.path.exists('openjs.json'):
            with open("openjs.json","r") as f :
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    nuser = User(username= user['username'], passw= user['passw'], email= user['email'])
                    
    def register(self, user: User):
        self.users.append(user)
        self.savetof()
        print("Kullanıcı Oluşturuldu")
    def  login(self):
        pass
    def savetof(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("openjs.json","w") as f :
            json.dump(list, f)
repos = UserRepo()
while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register \n"
                  "2- Login \n"
                  "3- logout \n"
                  "4- identity \n"
                  "5- çıkış \n ")
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("kullanıcı adı")
            passw = input("Şifreniz")
            email = input("email adresiniz")
            user = User(username= username, passw= passw, email= email)
            repos.register(user)

        elif secim == "2":
            pass
        elif secim == "3":
            pass
        elif secim == "4":
            pass
        else:
            print("Lütfen doğru bir seçim yapınız")
