from .menu_manager import MenuManager
from .user_manager import UserManager
from .colored_printer import ColoredPrinter


class App:
    """
    Application class.
    """

    def __init__(self):
        self.__menu = MenuManager()
        self.__user_manager = UserManager("data.json")

    def run(self) -> None:
        """
            Main program to register, show and login users.

            Returns:
            - None
        """
        try:
            while True:
                self.__menu.show()
                option = self.__menu.get_option()
                if option == 1:
                    self.__user_manager.register()
                elif option == 2:
                    self.__user_manager.print_data()
                elif option == 3:
                    self.__user_manager.login()
                elif option == 4:
                    break
        except KeyboardInterrupt:
            ColoredPrinter.cprint_failure(
                "Proceso principal interrumpido por el usuario.")
        except Exception as e:
            ColoredPrinter.cprint_failure(f"Ocurrión un error inesperado: {e}")
        else:
            ColoredPrinter.cprint_success(
                "Proceso principal terminado con éxito.")
