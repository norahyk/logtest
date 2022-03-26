import logging

from logtest.logging.submodule.sub_logging import sublog
_logger = logging.getLogger(__name__)


def log():
    _logger.error('logging root error')
    _logger.warning('logging root  warning')
    _logger.info('logging root  info')
    _logger.debug('logging root  debug')

    sublog()

if __name__ == "__main__":
    logger = logging.getLogger('logtest.logging')
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    logger.setLevel(logging.INFO)

    log()