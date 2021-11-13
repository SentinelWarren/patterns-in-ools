from patterns import Singleton


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

    def read(self) -> str:
        with open(self.file_name, "r") as log_file:
            return log_file.read()

    def __repr__(self) -> str:
        return (
            f"<class {self.__class__.__name__}("
            f"{self.file_name!r}) "
            f"at {hex(id(self))}>"
        )



if __name__ == '__main__':
    # print("<class '__main__.Logger'>" in Singleton._instances)
    # print(f"{len(Singleton._instances)}\n")

    # logger1 = Logger("class_logger.log")
    # logger2 = Logger("tst.txt")
    # print(logger1 is logger2)
    
    # logger2.file_name = "test/another_logger.log"
    # print(logger1.file_name is logger2.file_name)

    # print(f"\n{len(Singleton._instances)}")
    # print("<class '__main__.Logger'>" in Singleton._instances)
    print(Logger("class_logger.log"))
