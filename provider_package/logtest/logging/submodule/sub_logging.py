import logging

_logger = logging.getLogger(__name__)


def sublog():
    _logger.error('logging submodule error')
    _logger.warning('logging submodule warning')
    _logger.info('logging submodule info')
    _logger.debug('logging submodule debug')