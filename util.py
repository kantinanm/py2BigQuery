import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv('URL')+'/api/faculties'
print("URL env value:", URL)


def printHello():
    print("Hello Son")


def getFaculty(_token):
    print("getFaculty")
    print(URL)
    # print(_token)
    newHeaders = {'Content-type': 'application/json', 'Accepts': 'application/json',
                  'Authorization': 'Bearer {}'.format(_token)}
    # print(_token)

    response = requests.get(URL, headers=newHeaders)
    response.raise_for_status()
    print("Status code: ", response.status_code)

    response_Json = response.json()
    # print(response_Json)
    return json.dumps(response_Json)
