from patterns.singleton import Logger


def test_logger(tmpdir):
    logger = Logger(tmpdir.mkdir("temp").join("class_logger.log"))

    logger.critical("This is a critical message")
    logger.error("This is an error message")
    logger.warn("This is a warning message")
    logger.info("This is an info message")
    logger.debug("This is a debugging message")

    assert logger.read() == (
                                f"[CRITICAL] This is a critical message\n"
                                f"[ERROR] This is an error message\n"
                                f"[WARNING] This is a warning message\n"
                                f"[INFO] This is an info message\n"
                                f"[DEBUG] This is a debugging message\n"
                            )