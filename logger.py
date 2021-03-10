import logging
import json_logging


def get_logger():
    """
    Generic utility function to get logger object with fixed configurations
    :return:
    logger object
    """
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_non_web()
    logger = logging.getLogger(__name__)
    logging.basicConfig()
    json_logging.config_root_logger()
    logger.setLevel(logging.DEBUG)
    logging.addLevelName(logging.ERROR, 'error')
    logging.addLevelName(logging.WARNING, 'warning')
    logging.addLevelName(logging.INFO, 'info')
    logging.addLevelName(logging.DEBUG, 'debug')
    logger.addHandler(logging.NullHandler())
    return logger
