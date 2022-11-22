import random
import string
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

import xmltodict, json


class OVConnection(object):

    def __init__(self,
            email, password, appId, appSecret, hostaddress, secure=True, 
            useport=-1, debug=False):
        self.email       = email
        self.password    = password
        self.appId       = appId
        self.appSecret   = appSecret
        self.hostaddress = hostaddress
        self.secure      = secure
        self.useport     = useport
        self.debug       = debug
        self.token       = None
        self.token_type  = None

    def endpoint(self):
        #return "%s://%s/index.php?action=" % ("https" if self.secure == True else "http", self.hostaddress)
        return "%s://%s%s/" % (("http", "https")[self.secure == True], self.hostaddress, ('', ':' + str(self.useport))[str(self.useport) != '-1'])

    def login(self):
        # login endpoint https:// {hostaddress} /api/ov/v1/applications/authenticate
        authenticate_endpoint = '/api/ov/v1/applications/authenticate'
        headers = { 'Content-Type' :  'application/json; charset=utf-8' }  
        payload = {
        'email'      :   self.email,
        'password'   :   self.password,
        'appId'      :   self.appId,
        'appSecret'  :   self.appSecret
        }
        req = requests.post(self.endpoint() + authenticate_endpoint, json=payload, headers=headers)
        return req.status_code, req.json()

