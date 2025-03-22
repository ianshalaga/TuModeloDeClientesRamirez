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
                return json.load(file)
        except FileNotFoundError:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.read.__name__} | Archivo no encontrado.")
        except json.JSONDecodeError:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.read.__name__} | Archivo JSON inválido.")
        except Exception as e:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.read.__name__} | Unexpected error: {repr(e)}")

    def write(self, data: dict) -> None:
        """
        Write data into a json file.

        Args:
        - data (dict): Data to write into json file.

        Returns:
        - None
        """
        try:
            if not data:
                ColoredPrinter.cprint_warning(
                    f"Class: {__class__.__name__} | Method: {__class__.write.__name__} | Diccionario de datos vacío.")
                return
            with open(self._filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except TypeError:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.write.__name__} | Datos no serializables a JSON.")
        except PermissionError:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.write.__name__} | Permiso denegado para escribir en el archivo.")
        except OSError as e:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.write.__name__} | Error de sistema: {repr(e)}")
        except Exception as e:
            ColoredPrinter.cprint_failure(
                f"Class: {__class__.__name__} | Method: {__class__.write.__name__} | Unexpected error: {repr(e)}")
