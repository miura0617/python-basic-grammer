import contextlib


def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False

def cleanup():
    print('clean up')

# try ~ finally 処理をcontextlibを使って書いてみる
try:
    is_ok = is_ok_job()
    print('more task')
finally:
    if not is_ok:
        cleanup()
