import enum

db = {
    'stack1': 1,
    'stack2': 2,
}

# STATUS_ACTIVE = 1
# STATUS_INACTIVE = 2
# 
# if db['stack1'] == STATUS_ACTIVE:
#     print('shutdown')
# elif db['stack1'] == STATUS_INACTIVE:
#     print('terminate')


class Status(enum.IntEnum):         # IntEnumというのもある
    # サーバのステータスをイメージ
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

if db['stack1'] == Status.ACTIVE:   # IntEnumを使うと、左辺の表記が省略できる
    print('shutdown')
elif db['stack1'] == Status.INACTIVE:
    print('terminate')

