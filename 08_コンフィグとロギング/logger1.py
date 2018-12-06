""" logger でそれぞれのloggingを切り替えていく """
import logging

logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__) # ここでloggingの内容を root -> __main__ へ変更した
# こうすることで, どこでloggingしているか分かり易い

LOGGER.info('from main') # INFO:__main__:from main と表示
logging.info('from main') # INFO:root:from main と表示
