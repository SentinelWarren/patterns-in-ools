from patterns.singleton import Singleton, Logger


def test_singleton():
    logger1 = Logger("class_logger.log")
    logger2 = Logger("another_logger.log")

    assert "<class 'patterns.singleton.Logger'>" in str(Singleton._instances.keys())
    assert logger1 == logger2

    logger2.file_name = "another_logger.log"
    assert logger1.file_name == logger2.file_name
    