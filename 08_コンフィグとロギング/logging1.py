""" python のloggingは以下のものが保存できる
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

# logging.basicConfig(level=logging.INFO) # INFOレベルまでロギングされる
# logging.basicConfig(level=logging.DEBUG) # DEBUGレベルまでロギングされる
logging.basicConfig(filename='test.log', level=logging.DEBUG) # ロギング内容をtest.logに保存する

logging.critical('critical') # CRITICAL:root:critical と表示
logging.error('error') # ERROR:root:error と表示
logging.warning('warning') # WARNING:root:warning と表示
logging.info('info') # INFO:root:info と表示
logging.debug('debug') # DEBUG:root:debug と表示

logging.info('info {}'.format('test')) # INFO:root:info test と表示
logging.info('info %s %s' % ('test', 'test2')) # INFO:root:info test test2 と表示
logging.info('info %s %s', 'test', 'test2') # INFO:root:info test test2 と表示
