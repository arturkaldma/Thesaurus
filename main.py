import json
def get_answer(key):
    data = json.load(open("data.json"))
    return data[key]

word = input("The word I'm looking for: ")
l = get_answer(word)
answer = ' '.join([str(el) for el in l])
print(answer)