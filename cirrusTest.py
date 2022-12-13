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

orgId = "63295f10600b9a059807e6ff"
siteId = "63295f10600b9a58b807e700"

# status, data = ov.getSites(orgId)

# print(status, data)

status, data = ov.createGroup(orgId, siteId, group="ChaiChee")

print(status, data)



