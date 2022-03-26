import logging
from loguru import logger as _logger

from logtest.loguru.submodule.sub_loguru import sublog


def log():
    _logger.error('logging root error')
    _logger.warning('logging root  warning')
    _logger.info('logging root  info')
    _logger.debug('logging root  debug')

    sublog()

if __name__ == "__main__":
    import sys
    _logger.remove()
    _logger.add(sys.stderr, filter='logtest')
    # _logger.add(sys.stderr, filter='logtest.loguru.submodule')

    # logger = logging.getLogger('logtest.loguru.submodule.sub_loguru')
    # sh = logging.StreamHandler()
    # logger.addHandler(sh)
    # logger.setLevel(logging.INFO)

    log()