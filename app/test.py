import requests
from hashlib import sha256


# r = requests.post('http://0.0.0.0:8080/cafe/login', json={"username": "test_user", "password": "password"})
#
# print(r.status_code)
# print(r.text)
# print(sha256("password".encode('UTF-8')).hexdigest())



# r = requests.post('http://0.0.0.0:8080/cafe', json={"token": "test_user"})
# r = requests.get('http://0.0.0.0:8080/bot/cafes', headers={"token": "9ab4de56-f48b-4ce8-a3ee-884ba1f4e185"})
# r = requests.get('http://0.0.0.0:8080/bot/cafes/Druzi', headers={"token": "9ab4de56-f48b-4ce8-a3ee-884ba1f4e185"})
# r = requests.get('http://0.0.0.0:8080/bot/cafes/Druzi/categories', headers={"token": "9ab4de56-f48b-4ce8-a3ee-884ba1f4e185"})
# r = requests.get('http://0.0.0.0:8080/bot/cafes/Druzi/categories/59a811ee5f0a0a896baf56b5',
#                  headers={"token": "9ab4de56-f48b-4ce8-a3ee-884ba1f4e185"})
r = requests.get('http://0.0.0.0:8080/bot/cafes/Druzi/products', headers={"token": "9ab4de56-f48b-4ce8-a3ee-884ba1f4e185"})


print(r.status_code)
print(r.text)
