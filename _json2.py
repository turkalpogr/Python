import  json
#json to dict
with open("person.json") as f :
    data = json.load(f)
    print(data)
    print(data["name"])
#dict to json
person = {"name": "mahmut","languages": ["Python", "java"]}
result = json.dumps(person)
print(type(result))