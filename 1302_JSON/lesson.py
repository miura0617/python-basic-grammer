"""
<?xml version='1.0' encoding='utf-8'?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
</root>


{
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}
    
"""

import json


j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print('##################')
print(json.dumps(j))     # jsonの場合は、辞書型の変数をdumpsに入れるだけ

# ファイルに書き込む
with open('test.json', 'w') as f:
    json.dump(j, f)

