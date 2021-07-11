import logging
import logging.config

logger = logging.getLogger(__name__)

logger.error('Api call is failed')

# Key-Valueの形で書ける
# ログ解析やログのグラフ化をするような作業のとき活用できる
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})

