""" SMTPハンドラーでログをemailに送信する.
けど, emailが大量に届くことを防ぐために,
一度ログ解析ソフトにログを送ってから,
その解析結果をemailに送信するのが一般的です.
今回は練習のためにlogをemailに送信します. """
import logging.handlers

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'your_email@outlook.jp'
to_email = 'your_email@outlook.jp'
username = 'your_email@outlook.jp'
password = 'your_password'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port),
    from_email,
    to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
)) # critical とoutlookに送信されてます.

logger.info('test')
logger.critical('critical')
