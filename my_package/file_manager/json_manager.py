import json
from .base_manager import FileManager
from ..colored_printer import ColoredPrinter


class JsonFileManager(FileManager):
    """
    Json files manager.
    """

    def read(self):
        """
        Read data from a json file.

        Returns:
        - dict: Data from json file.
        """
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                ColoredPrinter.cprint_success(
                    "Lectura del archivo JSON exitosa.")
                return json.load(file)
        except FileNotFoundError:
            ColoredPrinter.cprint_failure("Archivo no encontrado.")
        except json.JSONDecodeError:
            ColoredPrinter.cprint_failure("Archivo JSON inválido.")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Unexpected error: {repr(e)}")

    def write(self, data):
        pass
