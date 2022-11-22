import requests
import aosAPI
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

switch = aosAPI.AOSConnection(
    username='admin',
    password='switch123',
    hostaddress='192.168.2.254',
    secure=False,
    debug=True
    )

# status, data = switch.save()
# status, data = switch.setContact(contact="Jerry")
# status, data = switch.setLocation(contact="Singapore")
# status, data = switch.setSystemName(contact="CORESW01")
# status, data = switch.setVLAN(vlan="7")
# status, data = switch.getVLAN(vlan="7")
# status, data = switch.setNTPServer()
# status, data = switch.getIPInterface(nameif='int-vl1')
# status, data = switch.setIPInterface(ipaddress='11.11.11.11', netmask='255.255.255.0', vlan='1')
# status, data = switch.getIPRoute()
# status, data = switch.setIPStaticRoute(subnet='11.11.11.11/32', gateway='1.1.1.1')
# status, data = switch.getInterface(interface='1/1/10')
# status, data = switch.getIntVlan(interface='1/1/1')
# status, data = switch.getIntVlan()
# status, data = switch.getChassisTemperature()

# print(data)





