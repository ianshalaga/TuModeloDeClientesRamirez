from my_package.file_manager import JsonFileManager
from my_package import ColoredPrinter

name = "file.json"
json_file = JsonFileManager(name)
json_file.read()

ColoredPrinter.cprint_info("INFO")
