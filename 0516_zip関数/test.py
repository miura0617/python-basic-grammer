days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tee', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# iが色んな所にあって読みにくいので、
print('#################')
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


