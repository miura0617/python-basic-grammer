import requests

# POST
r = requests.post(
   'http://127.0.0.1:5000/post', data={'username': 'mike'}
)

# PUT
#r = requests.put(
#    'http://127.0.0.1:5000/post', data={'username': 'mike'}
#)

# DELETE
#r = requests.delete(
#    'http://127.0.0.1:5000/post', data={'username': 'mike'}
#)

# GETの場合は、show_postのmethodプロパティで許可されてないので、返ってこない
#r = requests.get(
#    'http://127.0.0.1:5000/post', data={'username': 'mike'}
#)

print(r.text)
