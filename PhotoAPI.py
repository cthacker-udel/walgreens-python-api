import PhotoEndpoints
import requests
import json
import uuid

class PhotoAPI:
    def __init__(self,API_KEY,AffiliateID):
        self.api_key = API_KEY
        self.affiliateID = AffiliateID

    def fetch_upload_credentials(self,platform="ios",transaction="photocheckoutv2",app_version="default_version",device_details="details,default"):
        if app_version != 'default_version' and device_details != 'details,default':
            self.headers = {"apiKey": self.api_key,
                        "affId": self.affiliateID,
                        "platform": platform,
                        "transaction": transaction,
                        "appVer": app_version,
                        "devInf": device_details}
            url = PhotoEndpoints.fetch_credentials_sandbox_url
            response = requests.post(url,json=self.headers).json()
            return response['sasKeyToken']
        elif app_version != 'default_version':
            self.headers = {"apiKey": self.api_key,
                        "affId": self.affiliateID,
                        "platform": platform,
                        "transaction": transaction,
                        "appVer": app_version}
            url = PhotoEndpoints.fetch_credentials_sandbox_url
            response = requests.post(url,json=self.headers).json()
            return response['sasKeyToken']
        elif device_details != 'details,default':
            self.headers = {"apiKey": self.api_key,
                        "affId": self.affiliateID,
                        "platform": platform,
                        "transaction": transaction,
                        "devInf": device_details}
            url = PhotoEndpoints.fetch_credentials_sandbox_url
            response = requests.post(url,json=self.headers).json()
            return response['sasKeyToken']
        else:
            self.headers = {"apiKey":self.api_key,
                            "affId": self.affiliateID,
                            "platform": platform,
                            "transaction": transaction}
            url = PhotoEndpoints.fetch_credentials_sandbox_url
            response = requests.post(url,json=self.headers).json()
            return response['cloud'][0]['sasKeyToken']
    def generate_photo_upload_url(self,sas_key_token="GeneratedFromAboveMethod"):
        split_sas_key_token = sas_key_token.split('?')
        blobContainer = split_sas_key_token[0]
        signature = split_sas_key_token[1]
        imagename = 'Image-' + self.affiliateID + '-' + str(uuid.uuid4()) + '.jpg'
        return blobContainer + '/' + imagename + '?' + signature
    def upload_image(self,photo_upload_url,amount_of_image_bytes,_uuid,_uploadtype):
        headers = {'Content-Type': 'image',
                   'Content-Length': amount_of_image_bytes,
                   'x-ms-client-request-id': _uuid,
                   'x-ms-blob-type': _uploadtype}
        response = requests.put(photo_upload_url,data=headers)
        return response.status_code == 200






if __name__ == '__main__':
    photoApi = PhotoAPI('exampleAPIKEY','photoapi')
    photoApi.fetch_upload_credentials()
