import requests
import OVNodeAPI
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)


OVnodeURL = 'https://eu.manage.ovcirrus.com/api/ov/v1/applications/authenticate'

ov = OVNodeAPI.OVConnection(
    email='samuel.yip@al-enterprise.com',
    password='Ciscotac@123',
    hostaddress='eu.manage.ovcirrus.com',
    appId='637c83ada1a19baa83c664c3',
    appSecret='01fac5723d2dc2b1cb5a4f448f1f36064fa81d2ccf8d1df79898a385285d240f',
    debug=True
    )

    
# ov = OVNodeAPI.OVConnection(
#     email='samuel.yip@al-enterprise.com',
#     password='Ciscotac@123',
#     hostaddress='apac.manage.ovcirrus.com',
#     appId='637cacd9f61066758aec97ef',
#     appSecret='037f0757ef65a65ad99988ad4e68c926b645f6bad3a86f55fb9baaca9d22e5f5',
#     debug=True
#     )

status, data = ov.login()
print(status, data)

#https://manage.ovcirrus.com/api/ov/v1/organizations
status, data = ov.APIRequest('api/ov/v2/user/profile')
print(status, data)



