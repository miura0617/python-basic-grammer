l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# ここをラムダを使って簡単に書ける
def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)
