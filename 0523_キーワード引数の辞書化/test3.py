def menu(**kwargs):
    print(kwargs)      # 渡されたキーワード引数が、辞書型で保持されていることがわかる
    for k, v in kwargs.items():
        print(k, v)

#menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)             # 引数に辞書を与える方法もある
