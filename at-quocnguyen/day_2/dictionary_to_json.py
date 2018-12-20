import json

alphabet_letters = ["a", "b", "c"]

with open("alphabet_list.json", "w") as f:
    json.dump(alphabet_letters, f)

with open("alphabet_list.json", "r") as f:
    read_json_content = f.read()
    print (read_json_content)
