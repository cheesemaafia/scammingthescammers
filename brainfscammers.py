# TODO: Rotate IPs, make this more customizable
# importing all the required libraries
import requests
import json
import random

print("                                ,_-=(!7(7/zs_.
                             .='  ' .`/,/!(=)Zm.
               .._,,._..  ,-`- `,\ ` -` -`\\7//WW.
          ,v=~/.-,-\- -!|V-s.)iT-|s|\-.'   `///mK%.
        v!`i!-.e]-g`bT/i(/[=.Z/m)K(YNYi..   /-]i44M.
      v`/,`|v]-DvLcfZ/eV/iDLN\D/ZK@%8W[Z..   `/d!Z8m
     //,c\(2(X/NYNY8]ZZ/bZd\()/\7WY%WKKW)   -'|(][%4.
   ,\\i\c(e)WX@WKKZKDKWMZ8(b5/ZK8]Z7%ffVM,   -.Y!bNMi
   /-iit5N)KWG%%8%%%%W8%ZWM(8YZvD)XN(@.  [   \]!/GXW[
  / ))G8\NMN%W%%%%%%%%%%8KK@WZKYK*ZG5KMi,-   vi[NZGM[
 i\!(44Y8K%8%%%**~YZYZ@%%%%%4KWZ/PKN)ZDZ7   c=//WZK%!
,\v\YtMZW8W%%f`,`.t/bNZZK%%W%%ZXb*K(K5DZ   -c\\/KM48
-|c5PbM4DDW%f  v./c\[tMY8W%PMW%D@KW)Gbf   -/(=ZZKM8[
2(N8YXWK85@K   -'c|K4/KKK%@  V%@@WD8e~  .//ct)8ZK%8`
=)b%]Nd)@KM[  !'\cG!iWYK%%|   !M@KZf    -c\))ZDKW%`
YYKWZGNM4/Pb  '-VscP4]b@W%     'Mf`   -L\///KM(%W!
!KKW4ZK/W7)Z. '/cttbY)DKW%     -`  .',\v)K(5KW%%f
'W)KWKZZg)Z2/,!/L(-DYYb54%  ,,`, -\-/v(((KK5WW%f
 \M4NDDKZZ(e!/\7vNTtZd)8\Mi!\-,-/i-v((tKNGN%W%%
 'M8M88(Zd))///((|D\tDY\\KK-`/-i(=)KtNNN@W%%%@%[
  !8%@KW5KKN4///s(\Pd!ROBY8/=2(/4ZdzKD%K%%%M8@%%
   '%%%W%dGNtPK(c\/2\[Z(ttNYZ2NZW8W8K%%%%YKM%M%%.
     *%%W%GW5@/%!e]_tZdY()v)ZXMZW%W%%%*5Y]K%ZK%8[
      '*%%%%8%8WK\)[/ZmZ/Zi]!/M%%%%@f\ \Y/NNMK%%!
        'VM%%%%W%WN5Z/Gt5/b)((cV@f`  - |cZbMKW%%|
           'V*M%%%WZ/ZG\t5((+)L'-,,/  -)X(NWW%%
                `~`MZ/DZGNZG5(((\,    ,t\\Z)KW%@
                   'M8K%8GN8\5(5///]i!v\K)85W%%f
                     YWWKKKKWZ8G54X/GGMeK@WM8%@
                      !M8%8%48WG@KWYbW%WWW%%%@
                        VM%WKWK%8K%%8WWWW%%%@`
                          ~*%%%%%%W%%%%%%%@~
                             ~*MM%%%%%%@f`
                                 '''''")
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
