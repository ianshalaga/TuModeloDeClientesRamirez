import sys
from my_package import ColoredPrinter
from my_package import App

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ColoredPrinter.cprint_failure("Uso incorrecto.")
        ColoredPrinter.cprint_info(
            "Este programa no acepta argumentos de línea de comandos (flags / opciones).")
        exit()

    app = App()
    app.run()
