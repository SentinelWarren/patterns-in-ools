from pypatterns import Logger


def test_methods_return(tmpdir_factory):
    tmp = tmpdir_factory.mktemp("func")
    logger = Logger(tmp.join("logger.log"))
    expected = None

    assert logger.critical("This is a critical message") == expected
    assert logger.error("This is an error message") == expected
    assert logger.warn("This is a warning message") == expected
    assert logger.info("This is an info message") == expected
    assert logger.debug("This is a debugging message") == expected
    assert logger.print_log() == expected

def test_log_output():
    expected_log = (
        f"[CRITICAL] This is a critical message\n"
        f"[ERROR] This is an error message\n"
        f"[WARNING] This is a warning message\n"
        f"[INFO] This is an info message\n"
        f"[DEBUG] This is a debugging message\n"
    )
    assert Logger("logger.log")._read_log() == expected_log
