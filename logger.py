import logging
import json_logging
import sys


def _get_logger():
    json_logging.init_non_web(enable_json=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger


LOGGER = _get_logger()
