import json
try:
    person = '{"name": "mahmut","languages": ["Python", "java"]}'
    # result = person["languages"][1]
    result = json.loads(person)
    print(result["languages"][1])
except Exception as ex:
    pass
