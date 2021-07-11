import glob
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')            # 1つずつ指定しなければならない
    # z.write('test_dir/test.txt')   # 1つずつ指定しなければならない
    for f in glob.glob('test_dir/**', recursive=True):  # **(アスタリスク2つ)だとサブフォルダも探索してくれる
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')
    

