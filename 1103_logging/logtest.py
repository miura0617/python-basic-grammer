import logging 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # loggerを使うとmainと別ファイルでログレベルを変更できる

def do_something():
    #logging.info('from logtest info')  # loggerではなくloggingであるため、lesson3.py(メイン)のloggingとして呼ばれる
    logger.info('from logtest')
    logger.debug('from logtest debug')
