s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.txt', 'w') as f:
#     f.write(s)

with open('test.txt', 'r') as f:
    # print(f.read())  # 一度に全部読み込む
    while True:
        line = f.readline()  # 一行ずつ読み込む
        print(line, end='')  # ファイル内にも改行、print関数も自動で改行入れてしまうので２回改行されるのを防ぐ
        if not line:
            break


