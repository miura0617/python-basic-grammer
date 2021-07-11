import contextlib
import os

# somefile.tmpというファイルがあれば削除し、なければ何もしない
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

# 上記の処理は、以下のようにも書ける
# suppressは、「抑圧する」という意味
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
    os.remove('somefile.tmp')
    os.remove('somefile.tmp')
    os.remove('somefile.tmp')


