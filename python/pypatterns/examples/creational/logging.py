"""Example implementation of Singleton Pattern"""
from typing import Any
from pypatterns import singleton


class Logger(metaclass=singleton.SingletonMeta):
    """Logger class using Singleton pattern"""
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def _write_log(self, level: str, msg: Any) -> None:
        """Write a logging message depending on the level
        to the global log file"""
        with open(self.file_name, "a", encoding='utf-8') as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg: Any) -> None:
        """Log message of level critical"""
        self._write_log('CRITICAL', msg)
    
    def error(self, msg: Any) -> None:
        """Log message of level error"""
        self._write_log('ERROR', msg)

    def warn(self, msg: Any) -> None:
        """Log message of level warning"""
        self._write_log('WARNING', msg)

    def info(self, msg: Any) -> None:
        """Log message of level info"""
        self._write_log('INFO', msg)

    def debug(self, msg: Any) -> None:
        """Log message of level debug"""
        self._write_log('DEBUG', msg)

    def read_log(self) -> str:
        """Read the global log file"""
        with open(self.file_name, "r", encoding='utf-8') as log_file:
            return log_file.read()

    def print_log(self) -> None:
        """Print the log output to the console"""
        print(self.read_log())

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
    
