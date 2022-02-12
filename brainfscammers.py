import requests
import json
import random

def randomdig(n, start):
        if start == 0:
                string = ''
                for i in range(n):
                        string += str(random.randint(0, 9))
                return string
        else:
                string = str(start)
                for i in range(n):
                        string += str(random.randint(0, 9))
                return string

def randomstr(n):
        string = ''
        arr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#*'
        for i in range(n):
                string += arr[random.randint(0, 55)]
        return string

red_url = 'https://nadiyadigitalshope.link/1.php'

names = json.loads(open('names.json').read())

for name in names:
        username = name.lower() + randomdig(4, 0)
        phone = randomdig(9, 9)
        password = randomdig(4, 0) + randomstr(4)

        requests.post(red_url, allow_redirects = False, data = {
        'username': username,
        'password': password,
        'mobile number': phone
        })

        print("Entered " + username + "'s data!")

print("Scammer succesfully brainf***ed")
