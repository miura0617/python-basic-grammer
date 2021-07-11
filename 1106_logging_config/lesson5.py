import logging
import logging.config


logging.config.fileConfig('logging.ini')
#logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleExample')

# 本ファイルがsimpleExampleのロガーのため、logging.iniの設定によってdebugまで表示される
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
