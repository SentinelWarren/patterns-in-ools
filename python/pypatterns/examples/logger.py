from pypatterns import Singleton
from typing import Any


class Logger(metaclass=Singleton):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def _write_log(self, level: str, msg: Any) -> None:
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def _read_log(self) -> str:
        with open(self.file_name, "r") as log_file:
            return log_file.read()

    def critical(self, msg: Any) -> None:
        self._write_log('CRITICAL', msg)
    
    def error(self, msg: Any) -> None:
        self._write_log('ERROR', msg)

    def warn(self, msg: Any) -> None:
        self._write_log('WARNING', msg)

    def info(self, msg: Any) -> None:
        self._write_log('INFO', msg)

    def debug(self, msg: Any) -> None:
        self._write_log('DEBUG', msg)

    def print_log(self) -> None:
        print(self._read_log())

    def __repr__(self) -> str:
        return (
            f"<class {self.__class__.__name__}("
            f"{self.file_name!r}) "
            f"at {hex(id(self))}>"
        )



if __name__ == '__main__':
    logger = Logger("class_logger.log")
    logger.warn('AE-35 hardware failure predicted!')
    logger.print_log()
    
