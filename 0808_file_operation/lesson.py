import os
import pathlib
import glob
import shutil

print(os.path.exists('test.txt'))  # 存在するか確認
print(os.path.isfile('test.txt'))    # ファイルかどうか確認
print(os.path.isdir('design'))     # フォルダの存在確認

# os.rename('test.txt', 'renamed.txt') # ファイル名の書き換え
# os.symlink('renamed.txt', 'symlink.txt') # リンクファイルを作成(VSCを管理者権限で実行しないとエラー)

# os.mkdir('test_dir')  # ディレクトリ作成
# os.rmdir('test_dir')  # ディレクトリ削除

# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.copy('test_dir/test_dir2/empty.txt', \
#     'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))

# shutil.rmtree('test_dir')

print(os.getcwd())

