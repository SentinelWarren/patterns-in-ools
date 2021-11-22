"""Testing logging.Logger functionality"""
from pypatterns import logging


def test_methods_return(tmpdir_factory):
    """Test logging.Logger methods return"""
    tmp = tmpdir_factory.mktemp("func")
    log = logging.Logger(tmp.join("logger.log"))
    expected = None

    assert log.critical("This is a critical message") == expected
    assert log.error("This is an error message") == expected
    assert log.warn("This is a warning message") == expected
    assert log.info("This is an info message") == expected
    assert log.debug("This is a debugging message") == expected
    assert log.print_log() == expected

def test_log_output():
    """Test log file output"""
    expected_log = (
        "[CRITICAL] This is a critical message\n"
        "[ERROR] This is an error message\n"
        "[WARNING] This is a warning message\n"
        "[INFO] This is an info message\n"
        "[DEBUG] This is a debugging message\n"
    )
    assert logging.Logger("logger.log").read_log() == expected_log
