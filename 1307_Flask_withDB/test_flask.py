import requests

# GET
r = requests.get('http://127.0.0.1:5000/employee/jun')
print(r.text)

# POST
r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)

# PUT
r = requests.put('http://127.0.0.1:5000/employee', data={
   'name': 'jun', 'new_name': 'sakai'})
print(r.text)

# DELETE
r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)

