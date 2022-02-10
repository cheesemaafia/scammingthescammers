# TODO: Rotate IPs, make this more customizable
# importing all the required libraries
import requests
import json
import random

print(r'''                                              _J""-.
                  .-""L_                     /o )   \ ,';
             ;`, /   ( o\                    \ ,'    ;  /
             \  ;    `, /                     "-.__.'"\_;
             ;_/"`.__.-"
                          
                                                     
   fsc      ''')
print("Description: Short script for scamming the scammers with phishing links by brute forcing random data that makes sense. \n")

# input the url here (watch the accompanying youtube video to learn where to get this data from)
original_url = 'https://nadiyadigitalshope.link/1.php'
red_url = input(
    f"Enter the url of the website to attack/test: \n")


def randomdig(n, start):
    """This function returns a set of random digits"""
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
    """This function returns a set of random alphabets and special charectars"""
    string = ''
    arr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#*'
    for i in range(n):
        string += arr[random.randint(0, 55)]
    return string


# reading json data
names = json.loads(open('names.json').read())

# iterating over every items in the json file
for name in names:
    try:
        username = name.lower() + randomdig(4, 0)
        phone = randomdig(9, 9)
        password = randomdig(2, 0) + randomstr(2) + randomdig(2, 0) + randomstr(2)

        requests.post(red_url, allow_redirects = False, data = {
            # use your own data (watch the accompanying youtube video to learn where to get this data from)
            'username': username,
            'password': password,
            'mobile number': phone
        })

        print(
            f"Entered {username} with password: {password} and phone: {phone} succesfully!")
    except Exception as e:
        print(e)
        print("Unexpected error!")

# printing the final message
print("SCAMMER SUCCESSFULLY BRAINF***ED")
