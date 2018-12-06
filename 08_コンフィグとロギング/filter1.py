""" logging内容に保存してはいけないもの(例えばパスワード)などがある場合,
filterで判定して, 保存しないようにすることもできる.
"""
import logging

logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message # logメッセージの中にpasswordという文字列がなければTrueを返す.
    # Trueなので文字列は表示される.
    # Falseだと文字列は表示されない.

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter()) # ここでフィルターにかけてる.
logger.info('from main') # INFO:__main__:from main と表示.
logger.info('from main password = "test"') # logメッセージの中にpasswordという文字が含まれているので表示されない.
