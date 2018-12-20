import platform
import d3_file as file
import d3_json as json

x = platform.python_version()
print(x)

dataJSON = file.readData("./hello-python/datatest.json")
print("minify data: {0}".format(json.minify(dataJSON)))
print("beautify data: {0}".format(json.beautify(json.minify(dataJSON))))
dataTest = {
    "email": "hung.nguyen@asiantech.vn",
    "name": "Hung Nguyen V.",
    "nick_name": "Hung Dai Hiep"
}
file.create(json.beautify(dataTest), "./hello-python/myprofile.json")

dataTest["nick_name"] = "Lenh Ho Xung"
file.overwrite(json.beautify(dataTest), "./hello-python/myprofile.json")

file.delete("./hello-python/myprofile.json")
print("test delete file not exist:")
file.delete("./hello-python/myprofile.json")
