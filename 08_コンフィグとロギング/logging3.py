""" loggingをどこに書くかも重要です.
loggingを辞書形式で指定しておくと,
後々のloggingの解析が捗ります.
"""
import logging

logger = logging.getLogger(__name__)

logger.error('API call is failed') # このように書いてもいいですが,

logger.error({ # このように辞書形式で書いておくと, 後々解析が楽です.
    'action': 'create',
    'status': 'fail',
    'message': 'API call is failed'
})
# 後, loggerを置く場所も大切です.
# 経験値がものを言います.
