from .colored_printer import ColoredPrinter


class MenuManager:
    """
    Manage the application menu.
    """

    def __init__(self):
        self.__options = {
            1: "Registrar usuario",
            2: "Listar usuarios",
            3: "Iniciar sesión",
            4: "Salir",
        }

    def show(self) -> None:
        """
            Prints the menu.

            Returns:
            - None
        """
        try:
            ColoredPrinter.cprint_info("¿Qué desea hacer?")
            for option, description in self.__options.items():
                ColoredPrinter.cprint_info(f"Opción {option} -> {description}")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")

    def get_option(self) -> int:
        """
            Gets a menu option from the user.

            Returns:
            - option (int)
            - None if it fails.
        """
        try:
            option = int(input("Seleccione una opción: "))
            if option < 1 or option > len(self.__options):
                ColoredPrinter.cprint_failure(
                    "Opción inválida. Seleccione una de las opciones disponibles.")
                return
        except ValueError:
            ColoredPrinter.cprint_failure(
                "Opción inválida. Debe ingresar un número.")
        except KeyboardInterrupt:
            ColoredPrinter.cprint_failure(
                "Seleccione la opción correspondiente para finalizar el programa.")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")
        else:
            return option
