from abc import ABC, abstractmethod


class FileManager(ABC):
    '''
    Abstract base class for file management.

    Attributes:
    - __filename (str): Name of the file.
    '''

    def __init__(self, filename: str) -> None:
        """
        Initializes a FileManager instance.

        Args:
        - filename (str): Name of the file.
        """
        self._filename = filename

    # def get_filename(self) -> str:
    #     """
    #     Attr filename getter.

    #     Returns:
    #     - str: Name of the file.
    #     """
    #     return self.__filename

    # def set_filename(self, filename: str):
    #     """
    #     Attr filename setter.

    #     Args:
    #     - filename (str): Name of the file.

    #     Returns:
    #     - None
    #     """
    #     self.__filename = filename

    @abstractmethod
    def read(self):
        """
        Reads data from file.

        Returns:
        - Any: File content.
        """
        pass

    @abstractmethod
    def write(self, data):
        """
        Writes data into file.

        Args:
        - data (any): Data to be written.

        Returns:
        - None
        """
        pass
