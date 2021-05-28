import requests
from pprint import pprint

URL = 'http://www.python.org'

try:
    response = requests.get(URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:  # 200
        pprint(dict(response.headers))
        print('-' * 60)
        # response.content  raw content as bytes()
        # response.json()   raw JSON content converted to Python variables
        print(response.text)


print()
print("=" * 60)
print()

IMAGE_URL = "https://www.lbl.gov/wp-content/uploads/2018/01/mary_maxon.jpg"

try:
    response = requests.get(
        IMAGE_URL,
        timeout=(2.0, 10.0),
        # auth = ('student', 'l0lz'),
        # params = {
        #     'user': 'jstrickler@gmail.com',
        #     'key': "myauthkeyetcetc",
        # },
        # cookies = {
        #     'spam': "baljeoawiejfajewfi",
        #     'ham': "aowiejfaowiefjawoief",
        # },
        # proxies = {
        #     'https': 'proxy.lbl.doe.gov:123',
        # }
    )
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:  # 200
        pprint(dict(response.headers))
        print('-' * 60)
        file_name = "doe.jpg"
        with open(file_name, "wb") as file_out:
            file_out.write(response.content)


