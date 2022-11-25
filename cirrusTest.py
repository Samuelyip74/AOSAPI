import requests
import time
import OVCirrusAPIConsumables
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)


ov = OVCirrusAPIConsumables.OVConnection(
    email='samuel.yip@al-enterprise.com',
    password='Ciscotac@123',
    hostaddress='eu.manage.ovcirrus.com',
    appId='637c83ada1a19baa83c664c3',
    appSecret='01fac5723d2dc2b1cb5a4f448f1f36064fa81d2ccf8d1df79898a385285d240f',
    debug=True
    )

#status, data = ov.login()
#print(status, data)

# status, data = ov.getUserProfile()

# data = {
#   "firstname": "Samuel",
#   "lastname": "Yip",
#   "country": "Singapore",
#   "verified": True,
#   "companyName": "Alcatel Enterprise Pte Ltd",
#   "email": "samuel.yip@al-enterprise.com",
#   "closestRegion": "EMEA",


# }

# status, data = ov.updateUserProfile(data=data)

# data = {
#     "name": "Singapore LA",
#     "mspId": "63295f10600b9a85f007e6fe",
#     "countryCode": "SG",
#     "timezone": "Asia/Singapore",
#     "idleTimeout": 0
# }
# status, data = ov.createOrg(data=data)

data = {
    'name' : 'Singapore ALE Pte Ltd'
}

# while True:
#     status, data = ov.getUserProfile()
#     print(data)
#     time.sleep(500)

status, data = ov.getUserProfile()    
print(status, data)



