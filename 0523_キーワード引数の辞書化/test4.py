def menu(food, *args, **kwargs):
    print(food)            # 普通の引数
    print(args)            # 位置引数のタプル化
    print(kwargs)          # キーワード引数の辞書化

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

