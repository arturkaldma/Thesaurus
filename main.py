import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def get_answer(key):
    if key in data:
        return ' '.join([str(el) for el in data[key]])
    elif key.title() in data:
        return ' '.join([str(el) for el in data[key.title()]])
    elif key.upper() in data:
        return ' '.join([str(el) for el in data[key.upper()]])
    elif len(get_close_matches(key, data.keys())) > 0:
        w = get_close_matches(key, data.keys())[0]
        print("Did you mean %s instead? If yes type Y, if not type N" % w)
        a = input("Y/N: ")
        if a == "Y":
            return ' '.join([str(el) for el in data[w]])
        elif a == "N":
            return "Something is wrong! Try write the word correctly!"
        else:
            return "Wrong entry"
    else:
        return "Something is wrong! Try write the word correctly!"

word = input("The word I'm looking for: ").lower()
print(get_answer(word))
