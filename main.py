from my_package.file_manager import JsonFileManager
from my_package import ColoredPrinter

name = "file.json"
json_file = JsonFileManager(name)
# json_data = json_file.read()

# print(json_data)

data = {
    "uno": 1,
    "dos": 2
}

json_file.write(data)
