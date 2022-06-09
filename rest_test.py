import requests

url = "http://192.168.1.50/"

data = {
    'r':0,
    'g':0,
    'b':255
}

response = requests.post(url,data=data)

print(response)