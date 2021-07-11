import tasks


result = tasks.build_server.delay()
print('doing....')
print(result)
