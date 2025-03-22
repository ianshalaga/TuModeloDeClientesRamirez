from functools import partial
from termcolor import colored


class ColoredPrinter:
    """
    Manage color prints in terminal.
    """

    @staticmethod
    def __colored_print(text: str, color: str) -> None:
        """
            Prints text in console with color using termcolor library.

            Args:
            - text (str): Text to print in console.
            - color (str): Color for the text.

            Returns:
            - None
        """
        ctext = colored(text, color, attrs=["bold"])
        print(ctext)

    # colored_print function wrappers
    cprint_success = partial(__colored_print, color="green")
    cprint_warning = partial(__colored_print, color="yellow")
    cprint_failure = partial(__colored_print, color="red")
    cprint_info = partial(__colored_print, color="blue")
