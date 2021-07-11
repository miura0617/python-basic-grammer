"""
web_server:         # configparserと違って[]ではなく:(コロン)
  host: 127.0.0.1   # configparserと違って、インデントが半角空白2つ
  port: 80

db_server:
  host: 127.0.0.1
  port: 3306
"""

import yaml

with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)
  
