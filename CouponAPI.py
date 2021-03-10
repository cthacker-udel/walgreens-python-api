import CouponEndpoints
import requests

class CouponAPI:
    def __init__(self, API_KEY, affiliate_id, coupon_code="", act="", appver="", device_info="", product_details={}, product_id="", qty=""):
        if product_details is None:
            product_details = {}
        self.api_key = API_KEY
        self.affiliate_id = affiliate_id
        self.coupon_code = coupon_code
        self.act = act
        self.appver = appver
        self.device_info = device_info
        self.product_details = product_details
        self.product_id = product_id
        self.qty = qty
    def validate_coupon(self):
        headers = {'apiKey': self.api_key,
                   'affId': self.affiliate_id,
                   'couponCode': self.coupon_code,
                   'act': self.act,
                   'appVer': self.appver,
                   'devInf': self.device_info,
                   'productDetails': self.product_details,
                   'productId': self.product_id,
                   'qty': self.qty}

        response = requests.post(CouponEndpoints.sandbox_url,json=headers)
        print(response)






if __name__ == '__main__':
    couponApi = CouponAPI('LV04IoqmGg0PiydbYxs4o7QYBaqFikwJ','storesapi','TESTFORALL','#.#','###.##3','info',{'productId': '00000011'},'info','1')
    couponApi.validate_coupon()