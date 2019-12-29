import requests

class Github:
    def __init__(self):
        self.api = "https://api.github.com"
    def getUser(self, username):
        response = requests.get(self.api+'//users//'+username)
        return response.json()

github = Github()

while True:
    secim = input("1 Find user \n 2 Get repo \n 3 create \n 4 çıkış :" )

    if secim =='4':
        break
    else:
        if secim == '1':
            username = input("username ")
            res = github.getUser(username)
            print(res)
        elif secim == '2':
            pass
        elif secim == '3':
            pass
        else:
            print("Yanlış bir işlem yaptınız")