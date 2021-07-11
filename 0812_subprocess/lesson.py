import subprocess

# subprocess.run(['ls'])  # Mac
# subprocess.run(['ls', '-al'])  # Mac
subprocess.run(['dir'], shell=True) # Windows shellに直接指定したコマンドを送って実行
print('#####')

# 存在しないコマンドを実行したとき、エラーコードが返ってくる(ゼロ以外の値)
# r = subprocess.run('ls', shell=True)
# r = subprocess.run('lsa', shell=True)
r = subprocess.run('dir', shell=True)
print(r.returncode)

print('#####')

