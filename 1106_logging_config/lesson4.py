import logging
import logging.config


logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)

# 本ファイルがrootのため、logging.iniの設定によってwarningまで表示される
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
