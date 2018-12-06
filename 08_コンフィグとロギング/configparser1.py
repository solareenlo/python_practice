""" configparserはコンフィグファイルを扱うものです. """
import configparser
""" configparserで扱う形式は以下のような形
[DEFAULT]
debug = True

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
# コンフィグの書き込み方法
# CONFIG = configparser.ConfigParser()
# CONFIG['DEFAULT'] = {
#     'debug': True
# }
# CONFIG['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# CONFIG['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
# with open('config.ini', 'w') as config_file:
#     CONFIG.write(config_file)

# コンフィグの読み込み方法
CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
print(CONFIG['web_server']) # <Section: web_server> と表示
print(CONFIG['web_server']['host']) # 127.0.0.1 と表示
print(CONFIG['web_server']['port']) # 80 と表示

print(CONFIG['DEFAULT']['debug']) # True と表示
