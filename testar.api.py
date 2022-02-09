 #importing the requests library
import requests
from requests.exceptions import HTTPError

searchUser = input("Ange en användare: ")

for url in [f'https://api.github.com/users/{searchUser}/repos']:
    try:
        response = requests.get(url)
        myRepos  = response.json()

        size = len(myRepos)
        for x in range(0, size):
            print(myRepos[x]['name'])

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
