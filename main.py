import json

def get_answer(key):
    data = json.load(open("data.json"))
    return data[key]

print(get_answer("rain"))