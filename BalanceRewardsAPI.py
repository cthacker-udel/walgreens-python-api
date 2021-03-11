import requests
import BalanceRewardsEndpoints as endpoints
from pprint import pprint
import urllib
import random
from datetime import date
from datetime import datetime


def random_16_digit():
    return str(random.choice([1,2,3,4,5,6,7,8,9])) + ''.join([str(random.choice([0,1,2,3,4,5,6,7,8,9])) for x in range(15)])


class BalanceRewardsAPI:
    def __init__(self, api_key, affiliate_id):
        self.api_key = api_key
        self.affiliate_id = affiliate_id
        self.authorization_code = ''
        self.state = ''
        self.transaction_id = ''
        self.access_token = ''
        self.refresh_token = ''

    def request_authorization_code(self, response_type, scope, redirect_uri, channel, transaction_id, state):
        body = {'client_id': self.affiliate_id,
                'response_type': response_type,
                'scope': scope,
                'redirect_uri': redirect_uri,
                'channel': channel,
                'transaction_id': transaction_id,
                'state': state}
        response = requests.get(endpoints.sandbox_url_auth_code, params=body).json()
        pprint(response)
        self.authorization_code = response['auth_code']
        self.state = state
        self.transaction_id = transaction_id

    def request_oauth_tokens(self, redirect_uri, channel):
        body = {'grant_type': self.authorization_code,
                'act': 'getOAuthToken',
                'client_id': self.affiliate_id,
                'client_secret': self.api_key,
                'code': self.authorization_code,
                'redirect_uri': redirect_uri,
                'channel': channel,
                'transaction_id': self.transaction_id,
                'state': self.state
                }
        response = requests.get(endpoints.sandbox_url_auth_token, params=body).json()
        pprint(response)
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']

    def deactivate_oauth_tokens(self,channel):
        body = {'act': 'deactivateToken',
                'client_id': self.affiliate_id,
                'client_secret': self.api_key,
                'token': self.access_token,
                'channel': channel
                }
        response = requests.get(endpoints.sandbox_url_auth_token,params=body).json()
        pprint(response)
        return response['status'] == 'success'

    def post_activity_data(self,user_id,manufacturer_name,device_name):
        creates = []
        today = date.today()
        data_list = []
        value_dict = {}
        data = {'id': 'unique_id',
                'device_tracked': 'true or false',
                'timestamp': '{}'.format(datetime.now()),
                'type': 'activity_type',
                'value': value_dict}
        data_list.append(data)

        body = {'access_token': self.access_token,
                'affiliate_id': self.affiliate_id,
                'transaction_id': random_16_digit(),
                'date': '{}'.format(date.today()).replace('-','_'),
                'user_device_id': user_id,
                'manufacturer_name': manufacturer_name,
                'device_name': device_name,
                'data': data_list
            }
        creates.append(body)
        response = requests.post(endpoints.sandbox_activity_url + '?apiKey={}'.format(self.api_key),json=creates).json()
        pprint(response)
        return response['success_code'] == '2000'

    def requests_balance_reward_points(self):
        body = {'apiKey': self.api_key,
                'access_token': self.access_token,
                'affiliate_id': self.affiliate_id,
                'act': 'getBRPoints',
                'transaction_id': random_16_digit()
        }
        response = requests.get(endpoints.sandbox_request_points_url,params=body).json()
        pprint(response)








if __name__ == '__main__':
    api_class = BalanceRewardsAPI('exampleAPIKEY', 'brctest')
    api_class.request_authorization_code('code', 'steps', 'YOUR_REDIRECT_URI', '1', '1234567890123456', 'abcd1234xyz')
