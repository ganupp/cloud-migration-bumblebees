import requests
import json

class Requests:
    def __init__(self):
        pass

    def token_gen(self):
        url = 'https://login.microsoftonline.com/782ee8a9-08a6-4c1b-86f5-b083d7f1122f/oauth2/token'

        headers = {}
        payload= {
            'grant_type':'client_credentials',
            'client_id':'f0bb51a4-067f-443f-b377-1a1d8631050b',
            'client_s':'****',
            'resource':'https://management.azure.com/'
        }

        response = requests.request('POST', url, headers=headers, data=payload, verify=False)
        return json.loads(response.text)['access_token']
    

requests_instance = Requests()
token = requests_instance.token_gen()




