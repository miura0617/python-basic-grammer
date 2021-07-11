def say_something(*args):
    print(args)                # 引数argsはタプルに入れられていることがわかります
    for arg in args:           # 引数argsはタプルなので、forループで回せる
        print(arg)

say_something('Hi', 'Mike', 'Nance')

