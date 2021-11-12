from typing import Any, Dict


class Singleton(type):
    _instances = dict()

    def __call__(cls, *args: Any, **kwargs: Any) -> Dict[Any, str]:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
            cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def _write_log(self, level: str, msg: str) -> None:
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg: str) -> None:
        self._write_log("CRITICAL", msg)
    
    def error(self, msg: str) -> None:
        self._write_log("ERROR", msg)

    def warn(self, msg: str) -> None:
        self._write_log("WARNING", msg)

    def info(self, msg: str) -> None:
        self._write_log("INFO", msg)

    def debug(self, msg: str) -> None:
        self._write_log("DEBUG", msg)

    def read(self):
        with open(self.file_name, "r") as log_file:
            return log_file.read()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.file_name}, "
            f"{self.__class__.mro})")



if __name__ == '__main__':
    print(Logger("class_logger.log") is Logger("class_logger.log"))

    logger1 = Logger("class_logger.log")
    print(logger1.file_name)
    logger2 = Logger("another_logger.log")
    logger2.file_name = "another_logger.log"
    print(logger2.file_name, logger1.file_name)
    print(logger1.file_name is logger2.file_name)
    print(str(Singleton._instances.keys()))
    print(Logger("just_logger.log"))