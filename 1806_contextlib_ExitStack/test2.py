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

def cleanup2():
    print('clean up2')

# # try ~ finally 処理をcontextlibを使って書いてみる
# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()

with contextlib.ExitStack() as stack:
    stack.callback(cleanup)
    stack.callback(cleanup2)

    # デコレーターを使って、callbackを追加する方法もある
    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    # 成功していたら(エラーがなかれば)、stack内のものはpop_allですべて出す
    if is_ok:
        stack.pop_all()
    