import logging
import logging.config

# fileConfigではなく、dictConfigで同じこともできる
# logging.config.fileConfig('logging.ini')
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'sampleHandlers': {
        'class': 'logging.StreamHandler',
        'formatter': 'sampleFormatter',
        'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING,
    },
    'loggers': {
        'sampleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})

#logger = logging.getLogger(__name__)
logger = logging.getLogger('sampleExample')

# 本ファイルがsampleExampleのロガーのため、logging.iniの設定によってdebugまで表示される
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
