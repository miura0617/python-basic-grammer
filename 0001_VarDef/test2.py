# 型を指定することもできるが、Pythonは省略できるのであまり使わない表記です
num: int = 1
name: str = '1'

new_num = int(name)

print(num, type(num))
print(name, type(name))
print(new_num, type(new_num))
