def menu(**kwargs):
    print(kwargs)      # 渡されたキーワード引数が、辞書型で保持されていることがわかる
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='coffee')
