import ProductEndpoints
import requests

class ProductAPI:
    def __init__(self,API_KEY,affiliate_id,_act):
        self.api_key = API_KEY
        self.affiliate_id = affiliate_id
        self.act = _act

    def make_request(self):
        headers = {'apiKey': self.api_key,
                   'affId': self.affiliate_id,
                   'act': self.act}
        response = requests.post(ProductEndpoints.sandbox_url,json=headers).json()
        return response








if __name__ == '__main__':
    productAPI = ProductAPI('LV04IoqmGg0PiydbYxs4o7QYBaqFikwJ')
