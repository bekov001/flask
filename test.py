from requests import put, get, post, delete


a = get('http://127.0.0.1:5000/api/users')
print(a.json())

# a = get('http://127.0.0.1:5000/api/user/1')
# print(a.json())
#
# b = post('http://127.0.0.1:5000/api/users', json={'about': 'I`m the best', 'card': '123', 'email': '123123@lol.kz', 'id': 2, 'name': 'Arnur', 'surname': 'ELegndaa', "password": "123123213"})
# print(b.json())
#
# a = get('http://127.0.0.1:5000/api/users')
# print(a.json())
#
# b = delete('http://127.0.0.1:5000/api/user/1')
# print(b.json())
#
# a = get('http://127.0.0.1:5000/api/users')
# print(a.json())
#
b = put('http://127.0.0.1:5000/api/user/2', json={'about': 'I`m the cool', 'card': '404', 'email': '123123@gmail.kz', 'id': 2, 'name': 'Arnur', 'surname': 'ELegndaa', "password": "123123213"})
print(b.json())

a = get('http://127.0.0.1:5000/api/users')
print(a.json())
