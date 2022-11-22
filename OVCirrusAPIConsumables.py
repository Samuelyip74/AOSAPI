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
        self.expires_in  = None
        self.token_type  = None

    def endpoint(self):
        #return "%s://%s/index.php?action=" % ("https" if self.secure == True else "http", self.hostaddress)
        return "%s://%s%s/" % (("http", "https")[self.secure == True], self.hostaddress, ('', ':' + str(self.useport))[str(self.useport) != '-1'])

    def login(self):
        # login endpoint https://{hostaddress}/api/ov/v1/applications/authenticate
        authenticate_endpoint = 'api/ov/v1/applications/authenticate'
        header = { 'Content-Type' :  'application/json; charset=utf-8' }  
        payload = {
        'email'      :   self.email,
        'password'   :   self.password,
        'appId'      :   self.appId,
        'appSecret'  :   self.appSecret
        }
        req = requests.post(self.endpoint() + authenticate_endpoint, json=payload, headers=header, verify=False)
        try:
            if req.status_code == 200:
                data = req.json()
                self.token_type = data['token_type']
                self.token = data['access_token']
                self.expires_in = data['expires_in']
                return req.status_code, data
        except:
            return 500, None

# User profile API

    def getUserProfile(self):
        # login endpoint https://{hostaddress}/api/ov/v1/user/profile
        endpoint = '/api/ov/v1/user/profile'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None           

    def updateUserProfile(self, data):
        # login endpoint https://{hostaddress}/api/ov/v1/user/profile
        endpoint = '/api/ov/v1/user/profile'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.put(self.endpoint() + endpoint, headers=header, json=data, verify=False)    
            if req.status_code in [200, 400, 401, 406, 500]:
                return req.status_code, req.json()                              
            else:
                return req.status_code, None 
        except:
            return 500, None            

    def getUserMSPPermissionLvl(self, mspId):
        endpoint = '/api/ov/v1/msps/' + mspId + '/permissions'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None          
            
    def getUserOrganizationPermission(self):
        endpoint = '/api/ov/v1/organizations/permissions'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None   

    def getUserSitePermission(self):
        endpoint = '/api/ov/v1/sites/permissions'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None  


# MSP API

    def getUserMSP(self):
        endpoint = '/api/ov/v1/msps'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None   

    def getMSP(self, mspId):
        endpoint = '/api/ov/v1/msps/' + mspId

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 403, 404, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None      
            
    def updateMSP(self, mspId, data):
        endpoint = '/api/ov/v1/msps/' + mspId

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.put(self.endpoint() + endpoint, json=data, headers=header, verify=False)    
            if req.status_code in [200, 400, 401, 403, 404, 406, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None          

# Organization API

    def createOrg(self, data):
        endpoint = '/api/ov/v1/organizations'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.post(self.endpoint() + endpoint, json=data, headers=header, verify=False)    
            if req.status_code in [200, 201, 400, 401, 403, 404, 406, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None      

    def listAllUserOrg(self):
        endpoint = '/api/ov/v1/organizations'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None                     

    def listAllOrgOfMSP(self, mspId):
        endpoint = '/api/ov/v1/msps/' + mspId + '/organizations'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 403, 404, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None                     

    def listAllOrgOfMSPSummary(self, mspId):
        endpoint = '/api/ov/v1/msps/' + mspId + '/organizations/summary'

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 403, 404, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None                     

    def getOrganization(self, orgId):
        endpoint = '/api/ov/v1/organizations/' + orgId 

        header = { 
            'Content-Type' :  'application/json; charset=utf-8',
            'Authorization' : self.token_type + ' ' + self.token
            }

        try:
            req = requests.get(self.endpoint() + endpoint, headers=header, verify=False)    
            if req.status_code in [200, 401, 403, 404, 500]:
                return req.status_code, req.json()                              

            else:
                return req.status_code, None 
        except:
            return 500, None    
               



