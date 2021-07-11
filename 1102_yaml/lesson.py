"""
web_server:         # configparserと違って[]ではなく:(コロン)
  host: 127.0.0.1   # configparserと違って、インデントが半角空白2つ
  port: 80

db_server:
  host: 127.0.0.1
  port: 3306
"""

import yaml

with open('config.yml', 'r') as yaml_file:
  data = yaml.load(yaml_file)
  print(data, type(data))
  print(data['web_server']['host'])
  print(data['web_server']['port'])
  print(data['db_server']['host'])
  print(data['db_server']['port'])
