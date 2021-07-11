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

print('@@@@@@@@@@@@@@@@@')
a = json.dumps(j)
print(json.loads(a))
print('@@@@@@@@@@@@@@@@@')

# ファイルに書き込む
with open('test.json', 'w') as f:
    json.dump(j, f)

print('##################')

# ファイルに読み込む
with open('test.json', 'r') as f:
    print(json.load(f))
