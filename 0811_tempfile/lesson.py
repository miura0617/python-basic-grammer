import tempfile  # pythonがI/Oバッファ上にtempfileを作って最後は自動で削除してくれる


# with文が完了するとtempfileはなくなる
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# with文が完了してもtempfileを消さないこともできる
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)    # どこにtempfileを作成したか表示する
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# テンポラリーディレクトリも作成できる
# zipファイル作成時に使われたりします
with tempfile.TemporaryDirectory() as td:
    print(td)

# テンプラリーディレクトリを消さずに残すこともできる
# テスト時に使われたりします
temp_dir =  tempfile.mkdtemp()
print(temp_dir)
