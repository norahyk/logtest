import logging
from loguru import logger

from logtest.logging.main import log as logging_log
from logtest.loguru.main import log as loguru_log


_logger = logging.getLogger(__name__)

def setup_logger():
    fmt = '%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s'
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(fmt))
    sh.setLevel(logging.INFO)
    _logger.addHandler(sh)
    _logger.setLevel(logging.INFO)

    pkg_logger = logging.getLogger('logtest')
    pkg_logger.addHandler(sh)
    pkg_logger.setLevel(logging.ERROR)

    logger.add(sh, level=logging.WARNING)
    logger.add('submodule.log', filter='logtest.loguru.submodule')



def main():
    setup_logger()
    _logger.info('run')
    logging_log()
    loguru_log()
    _logger.info('finish')


if __name__ == '__main__':
    main()