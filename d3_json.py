import json

def minify(data):
    if type(data) is not dict:
        data = json.loads(data)
    return json.dumps(data, separators=(",", ":"))

def beautify(data):
    if type(data) is not dict:
        data = json.loads(data)
    return json.dumps(data, indent=4)
