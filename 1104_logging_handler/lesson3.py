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

logging.info('info')

logger = logging.getLogger(__name__)
#logger.info('from main')

logtest.do_something()