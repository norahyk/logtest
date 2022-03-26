import logging
from loguru import logger as loguru_logger

__version__ = '0.1.0'

logger = logging.getLogger('logtest')
logger.addHandler(logging.NullHandler())


loguru_logger.remove()
