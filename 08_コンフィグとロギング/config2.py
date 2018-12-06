""" loggingの表示形式を直接同じファイルに辞書形式で指定することもできる. """
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING
    },
    'roggers': {
        'simpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagete': 0
        }
    }
})

LOGGER = logging.getLogger('simpleExample')

LOGGER.debug('debug message')
LOGGER.info('info message')
LOGGER.warning('warn message')
LOGGER.error('error message')
LOGGER.critical('critical message')
""" 上記の設定で
2018-12-06 13:50:23,815 simpleExample WARNING  warn message
2018-12-06 13:50:23,815 simpleExample ERROR    error message
2018-12-06 13:50:23,815 simpleExample CRITICAL critical message
と表示される
"""
