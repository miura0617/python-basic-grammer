"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

import logging

# loggingには表示レベルがある
# 以下を実行すると、CRITICAL~WARNINGを表示だったのが、CRITICAL~INFOまで表示するようになる
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='test.log', level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

#logging.critical('critical')
#logging.error('error')
#logging.warning('warning')
#logging.info('info')
#logging.debug('debug')

#logging.info('info {}'.format('test'))
logging.info('info %s %s', 'test', 'test2')

