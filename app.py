import requests
import os
from dotenv import load_dotenv
from util import *

load_dotenv()
token = ''
flag = 0  # for check finally

# GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
# SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
# STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
URL = os.getenv('URL')+'/api/login'
PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')

print('app.py run.')
print("URL env value:", URL)
print("Password env value:", PASSWORD)

newHeaders = {'Content-type': 'application/json'}
payload = {'email': USER, 'password': PASSWORD}

print('Before send data.')
# data=payload
try:
    # A get request to the API
    response = requests.post(URL, headers=newHeaders, json=payload)
    response.raise_for_status()
    print("Status code: ", response.status_code)

    response_Json = response.json()
    resultObj = json.loads(json.dumps(response_Json))
    # print(response_Json)

    if (response.status_code == 200):

        # print(response_Json['error'])
        # if ((resultObj['error']) != ''):
        # raise Exception(response_Json['error'])
        # print('no')
        # print(response_Json['error'])

        if (resultObj['success'] == True):
            token = resultObj['token']
            # print(response_Json['token'])

        print('get token ok.')
        flag = 1
        print('Token is ', token)
        # call sub function
        result = getFaculty(token)
        print("Converting JSON encoded data into Python dictionary")
        json_object = json.loads(result)

        for key, value in json_object['data'].items():
            print(key, ":", value)
        print("Done reading json file")

        # print(result)


# If the request fails (404) then print the error.
except requests.exceptions.HTTPError as error:
    print(error)
except Exception as error:
    print('fail ', error)
finally:
    if (flag == 1):
        print('Job done!')
    else:
        print('Job don\'t completed!')
