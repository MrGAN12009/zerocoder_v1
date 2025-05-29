import requests

adr = "http://193.168.46.127:8080/login"

data = {
    'login': "testuser",
    'password': "testuser"
}


r = requests.post(adr, json=data)

print(r)
print(r.content)
#commit changes comment