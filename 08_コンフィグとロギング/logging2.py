""" ロギングの表示内容をformatで変更できる """
import logging

# FORMATTER = '%(levelname)s:%(message)s' # INFO:info test test2 と表示
FORMATTER = '%(asctime)s:%(message)s' # 時間:info test test2 と表示

logging.basicConfig(level=logging.INFO, format=FORMATTER)

logging.info('info %s %s', 'test', 'test2')
