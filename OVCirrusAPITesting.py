import requests
import OVNodeAPI
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)


OVnodeURL = 'https://eu.manage.ovcirrus.com/api/ov/v1/applications/authenticate'

headers = { 'Content-Type' :  'application/json; charset=utf-8' }                    

payload = {
   'email'      :   'samuel.yip@al-enterprise.com',
   'password'   :   'Ciscotac@123',
   'appId'      :   '637c83ada1a19baa83c664c3',
   'appSecret'  :   '01fac5723d2dc2b1cb5a4f448f1f36064fa81d2ccf8d1df79898a385285d240f'
}

ov = OVNodeAPI.OVConnection(
    email='samuel.yip@al-enterprise.com',
    password='Ciscotac@123',
    hostaddress='eu.manage.ovcirrus.com',
    appId='637c83ada1a19baa83c664c3',
    appSecret='01fac5723d2dc2b1cb5a4f448f1f36064fa81d2ccf8d1df79898a385285d240f',
    debug=True
    )

status, data = ov.login()
print(status, data)

