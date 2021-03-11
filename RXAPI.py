import requests
import RXEndpoints
from pprint import pprint

class RXAPI:
    def __init__(self,api_key,affiliate_id):
        self.api_key = api_key
        self.affiliate_id = affiliate_id
        self.refill_landing_url = ''
        self.refill_access_token = ''
        self.transfer_access_token = ''
        self.custom_template = ''
        self.transfer_landing_url = ''

    def obtain_refill_landing_url(self,transaction,act,view):
        body = {'apiKey': self.api_key,
                'affId': self.affiliate_id,
                'transaction': transaction,
                'act': act,
                'view': view}
        url = RXEndpoints.sandbox_url
        response = requests.post(url,json=body).json()
        pprint(response)
        self.refill_landing_url = response['landingUrl']
        self.refill_access_token = response['token']
        self.custom_template = response['template']

    def open_refill(self,rx_number,app_id,act):
        body = {'affId': self.affiliate_id,
                'token': self.refill_access_token,
                'rxNo': rx_number,
                'appID': app_id,
                'act': act}
        url = self.refill_landing_url
        response = requests.post(url,json=body)
        pprint(response)

    def obtain_transfer_landing_url(self,transaction,act,view):
        body = {'apiKey': self.api_key,
                'affId': self.affiliate_id,
                'transaction': transaction,
                'act': act,
                'view': view}

        url = RXEndpoints.sandbox_url
        response = requests.post(url,json=body).json()
        pprint(response)
        self.transfer_landing_url = response['landingUrl']
        self.transfer_access_token = response['token']
        self.custom_template = response['template']

    def open_transfer(self,rx_image,app_id,act):
        body = {'affId': self.affiliate_id,
                'token': self.transfer_access_token,
                'rxImg': rx_image,
                'appID': app_id,
                'act': act}
        url = self.transfer_landing_url
        response = requests.post(url,json=body).json()
        pprint(response)







if __name__ == '__main__':
    rxapi = RXAPI('exampleapi','rxapi')
    rxapi.obtain_refill_landing_url('example','example','example')
