""" yaml もコンフィグファイルを扱う """
import yaml

# yaml でコンフィグファイルを書き込み方法
# with open('config.yml', 'w') as yaml_file:
#     yaml.dump({
#         'web_server': {
#             'host': '127.0.0.1',
#             'port': 80
#         },
#         'db_server': {
#             'host': '127.0.0.1',
#             'port': 3306
#         }
#     }, yaml_file, default_flow_style=False)
""" 出力は
db_server:
  host: 127.0.0.1
  port: 3306
web_server:
  host: 127.0.0.1
  port: 80
"""

# yaml でコンフィグファイルを読み込む方法
with open('config.yml', 'r') as yaml_file:
    DATA = yaml.load(yaml_file)
    print(DATA, type(DATA)) # {'db_server': {'host': '127.0.0.1', 'port': 3306},\
        #  'web_server': {'host': '127.0.0.1', 'port': 80}} <class 'dict'> と表示
    print(DATA['web_server']['host']) # 127.0.0.1 と表示
    print(DATA['web_server']['port']) # 80 と表示
    print(DATA['db_server']['host']) # 127.0.0.1 と表示
    print(DATA['db_server']['port']) # 3306 と表示
