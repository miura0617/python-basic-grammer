import re


# Greedy（欲深いという意味）
s = '<html><head><title>Title</title></head></html>'

print(re.match('<.*>', s))      # 文字が0個以上なので、最後まで見にいく
print(re.match('<.*?>', s))     # <html>だけヒットさせるには

