""" handler を使って, どこにloggingを保存するとかを決める.
いろんなことができるhandlerがあるので調べてみてね.
"""
import logging

logging.basicConfig(level=logging.INFO) # INFOレベルまでloggingするよ. という意味.

LOGGER = logging.getLogger(__name__) # getLogger で, どこのファイルでloggingしてるか指定する.

H = logging.FileHandler('logtest.log')
LOGGER.addHandler(H) # LOGGERのloggingの内容をlogtest.logに保存するよ. という意味.

LOGGER.info('from main logger') # INFO:__main__:from main logger と表示
logging.info('form main logging') # INFO:root:form main logging と表示
