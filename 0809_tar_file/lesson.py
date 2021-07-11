import tarfile

# tar.gzファイルに圧縮
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# tar.gzファイルを解凍
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')
