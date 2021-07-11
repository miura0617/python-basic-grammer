f = open('test.txt', 'w')
f.write('Test\n') # write()の方が読みやすいので使われる
print('I am print', file=f)  # print関数でもファイル書き込みできる
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

