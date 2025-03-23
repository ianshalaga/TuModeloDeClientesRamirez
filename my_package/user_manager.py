from .colored_printer import ColoredPrinter
from .file_manager.json_manager import JsonFileManager


class User:  # Cliente
    def __init__(self, user_name, user_pass):
        self.__user_name = user_name
        self.__user_pass = user_pass

    def get_user_name(self) -> str:
        return self.__user_name

    def get_user_pass(self) -> str:
        return self.__user_pass

    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def set_user_pass(self, user_pass: str):
        self.__user_pass = user_pass

    def __str__(self) -> str:
        return f"User: {self.__user_name} | Password: {self.__user_pass}"


class UserManager:
    """
    Manage users data.
    """

    def __init__(self, filename):
        self.__filename = filename
        self.__json_file_obj = JsonFileManager(self.__filename)

    def register(self) -> None:
        '''
            Register a user in the database.

            Returns:
            - None
        '''
        try:
            user_data = self.__json_file_obj.read()

            user_name = input("Ingrese un nombre de usuario:\n").strip()
            if not user_name:
                ColoredPrinter.cprint_failure(
                    "El nombre de usuario no puede estar vacío.")
                return

            if user_name in user_data:
                ColoredPrinter.cprint_warning(
                    f"El usuario {user_name} ya está registrado.")
                return

            user_pass = input("Ingrese una contraseña:\n").strip()
            if not user_pass:
                ColoredPrinter.cprint_failure(
                    "La contraseña no puede estar vacía.")
                return

            user_data[user_name] = user_pass
            self.__json_file_obj.write(user_data)
            ColoredPrinter.cprint_success(
                f"Usuario {user_name} registrado con éxito.")

        except KeyboardInterrupt:
            ColoredPrinter.cprint_failure(
                "Proceso de registro interrumpido por el usuario.")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")

    def login(self) -> None:
        """
        Allows an user to login.

        Returns:
        - None
        """
        try:
            user_data = self.__json_file_obj.read()

            user_name = input("Ingrese el nombre de usuario:\n").strip()
            if not user_name:
                ColoredPrinter.cprint_failure(
                    "El nombre de usuario no puede estar vacío.")
                return

            if user_name not in user_data:
                ColoredPrinter.cprint_warning(
                    f"El usuario {user_name} no está registrado.")
                return

            user_pass = input("Ingrese la contraseña de usuario:\n")
            if user_data[user_name] != user_pass:
                ColoredPrinter.cprint_failure("Contraseña incorrecta.")
                return

            ColoredPrinter.cprint_success("Inicio de sesión exitoso.")
        except KeyboardInterrupt:
            ColoredPrinter.cprint_failure(
                "Proceso de login interrumpido por el usuario.")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")

    def print_data(self) -> None:
        """
            Prints DB data.

        Returns:
        - None
        """
        try:
            user_data = self.__json_file_obj.read()

            if not user_data:
                ColoredPrinter.cprint_warning(
                    "La base de datos no contiene usuarios.")
                return

            for user, password in user_data.items():
                user_obj = User(user, password)
                ColoredPrinter.cprint_info(user_obj)
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")
