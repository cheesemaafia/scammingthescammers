#importing all the required libraries
import requests
import json
import random

#this function returns a set of random digits
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
#this function returns a set of random alphabets and special charectars
def randomstr(n):
        string = ''
        arr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#*'
        for i in range(n):
                string += arr[random.randint(0, 55)]
        return string

#input here the url 
red_url = 'https://nadiyadigitalshope.link/1.php'

#reading json data
names = json.loads(open('names.json').read())

#iterating over every items in the json file 
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

#printing the final message
print("Scammer succesfully brainf***ed")
