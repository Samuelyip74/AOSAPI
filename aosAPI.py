
import random
import string
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

import xmltodict, json


# def get_random_string(length):
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str

class AOSConnection(object):

    def __init__(self,
            username, password, hostaddress, secure=True, 
            useport=-1, debug=False):
        self.username    = username
        self.password    = password
        self.hostaddress = hostaddress
        self.secure      = secure
        self.useport     = useport
        self.debug       = debug

    def get_cookie(self):
        payload = {
            'username' :    self.username,
            'password'  :   self.password
        }
        header = {'Accept': 'application/vnd.alcatellucentaos+json'}                    

        response = requests.get(self.endpoint() +'auth/', payload, verify=False, headers=header)
        return response.cookies.get_dict()

    def endpoint(self):
        #return "%s://%s/index.php?action=" % ("https" if self.secure == True else "http", self.hostaddress)
        return "%s://%s%s/" % (("http", "https")[self.secure == True], self.hostaddress, ('', ':' + str(self.useport))[str(self.useport) != '-1'])

    def command(self, domain, urn = '', args = {}):
        if self.debug:
            print("GET Request: [ %s%s%s%s ]" % (
                    self.endpoint(),
                    '?' + domain,
                    '&' + urn,            
                    '=' + args))

        session_cookie = self.get_cookie()
        header = {'Accept': 'application/vnd.alcatellucentaos+json'}                    
        try:
            req = requests.get(self.endpoint() + domain + '/' + urn + '?' + args,verify=False, cookies=session_cookie, headers=header)
            return req.status_code, req.json()
        except:
            return 501, None     

    def info(self, domain, urn = '', args = {}):
        if self.debug:
            print("GET Request: [ %s%s%s%s ]" % (
                    self.endpoint(),
                    '?' + domain,
                    '&' + urn,            
                    '=' + args))

        session_cookie = self.get_cookie()
        header = {'Accept': 'application/vnd.alcatellucentaos+json'}                    
        try:
            req = requests.get(self.endpoint() + domain + '/' + urn + '?' + args,verify=False, cookies=session_cookie, headers=header)
            return req.status_code, req.content()
        except:
            return 501, None                 

    def save(self, sync = True):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=write+memory" + "%s" %  (("+flash-synchro", "")[sync == False])
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data

    def setContact(self, contact = ""):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=system+contact+" + contact
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data    

    def setSystemName(self, name = "Switch"):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=system+name+" + name
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data        

    def setLocation(self, location = ""):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=system+location+" + location
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data         

    def setNTPServer(self, server = "clock3.ovcirrus.com"):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=ntp+server+" + server
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data   

    def setTimezone(self, timezone = "ZP8"):
        domain = 'cli'
        urn = 'aos'
        args = "cmd=system+timezone+" + timezone
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data                     

    def getVLAN(self, vlan = None):
        domain = 'cli'
        urn = 'aos'
        if vlan:
            args = 'cmd=show+vlan+'  + vlan
        else:
            args = 'cmd=show+vlan'  
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data

    def setVLAN(self, name = "", vlan = None, state = 'enable'):
        domain = 'cli'
        urn = 'aos'
        if vlan is None:
            return None, None
        else:
            args = "cmd=vlan+" + vlan + "%s%s" %  (("+name+" + name, "")[len(str(name)) <= 0], "+admin-state+" + state)
        
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data

    def getIPInterface(self, nameif = ""):
        domain = 'cli'
        urn = 'aos'
        args = 'cmd=show+ip+interface+'  + nameif
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data        

    def setIPInterface(self, ipaddress, netmask, vlan, nameif = None):
        domain = 'cli'
        urn = 'aos'

        if nameif is None:
            nameif = 'int' + '-' + ipaddress + '-vl' + vlan

        args = 'cmd=ip+interface+'  + str(nameif) + '+address+' + ipaddress + '+mask+' + netmask + '+vlan+' + vlan
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data  

    def getIPRoute(self):
        domain = 'cli'
        urn = 'aos'
        args = 'cmd=show+ip+routes'
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data   

    def setIPStaticRoute(self, subnet, gateway, metric = '1'):
        domain = 'cli'
        urn = 'aos'
        args = 'cmd=ip+static-route+'  + subnet + '+gateway+' + gateway + '+metric+' + metric
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data    

    def getInterface(self, interface = None):
        domain = 'cli'
        urn = 'aos'

        if interface:
            args = 'cmd=show+interfaces+' + interface
        else:
            args = 'cmd=show+interfaces+status'
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data 

    def getIntVlan(self, interface = None):
        domain = 'cli'
        urn = 'aos'

        if interface:
            args = 'cmd=show+vlan+members+port+' + interface
        else:
            args = 'cmd=show+vlan+members'
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data         

    def setIntVlan(self, intRange, vlan, tagged=False):
        domain = 'cli'
        urn = 'aos'
        args = 'cmd=vlan+' + vlan + '+members+port+' + intRange + "%s" %  (("+tagged", "+untagged")[tagged == False])
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data        

    def getChassisTemperature(self):
        domain = 'mib'
        urn = 'chasEntTemperatureTable'
        args = 'mibObject0=chasEntTempCurrent&mibObject1=chasEntTempThreshold&mibObject2=chasEntTempDangerThreshold'
 
        status, data = self.command(domain=domain, urn=urn, args=args)
        return status, data['result']['data']['rows']['65']                                  
          
