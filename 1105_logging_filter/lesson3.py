"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

import logtest


# mainファイルのログレベルはINFO
logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter()) # フィルタ追加
logger.info('from main')
logger.info('from main password="test"') # 誤ってpassword情報までログに記録してしまう
