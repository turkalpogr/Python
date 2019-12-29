import requests
import json

api = "https://api.exchangeratesapi.io/latest?base="

bozulan = input("Bozulan döviz: ")
alinan = input("Alınan döviz : ")
miktar = int(input(f"Ne kadar {bozulan} alamk istiyorsunuz"))
result = requests.get((api + bozulan))
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan,result["rates"][alinan], alinan))
print(f"{bozulan} {miktar} = {alinan} {miktar*result['rates'][alinan]}")