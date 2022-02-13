# TODO: implement threading to make this much more fast and efficient
# TODO: make this more customizable

import requests
import json
import random
import string

# enter the url to test/attack here
red_url = 'https://nadiyadigitalshope.link/1.php'


def randomdig(n, start):
    if start == 0:
        random_number = ''
        for i in range(n):
            random_number += str(random.randint(0, 9))
        return random_number
    else:
        random_number = str(start)
        for i in range(n):
            random_number += str(random.randint(0, 9))
        return random_number


def randomstr(n):
    random_string = ''
    arr = string.ascii_letters + '!@#*'
    for i in range(n):
        random_string += arr[random.randint(0, len(arr))]
    return random_string


names = json.loads(open('names.json').read())

for name in names:
    username = name.lower() + randomdig(4, 0)
    phone = randomdig(9, 9)
    password = randomdig(4, 0) + randomstr(4)

    try:
        requests.post(red_url, allow_redirects=False, data={
            'username': username,
            'password': password,
            'mobile number': phone
        })

        print(f"Entered {username}'s data!")
    except:
        print("Error sending data")

print("Scammer succesfully brainf***ed")
