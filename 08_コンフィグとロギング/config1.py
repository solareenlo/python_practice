""" logging の形式を別ファイルに書いておくこともできるし,
直にこのファイルに書いておくこともできる.
"""
import logging.config

logging.config.fileConfig('logging.ini')
# logger = logging.getLogger(__name__)
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
""" 上記の設定だと
2018-12-06 13:24:44,373 __main__     WARNING  warn message
2018-12-06 13:24:44,373 __main__     ERROR    error message
2018-12-06 13:24:44,373 __main__     CRITICAL critical message
と表示される.
"""

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
""" 上記の設定だと
2018-12-06 13:29:19,513 simpleExample DEBUG    debug message
2018-12-06 13:29:19,513 simpleExample DEBUG    debug message
2018-12-06 13:29:19,513 simpleExample INFO     info message
2018-12-06 13:29:19,513 simpleExample INFO     info message
2018-12-06 13:29:19,514 simpleExample WARNING  warn message
2018-12-06 13:29:19,514 simpleExample WARNING  warn message
2018-12-06 13:29:19,514 simpleExample ERROR    error message
2018-12-06 13:29:19,514 simpleExample ERROR    error message
2018-12-06 13:29:19,514 simpleExample CRITICAL critical message
2018-12-06 13:29:19,514 simpleExample CRITICAL critical message
と表示される
"""
