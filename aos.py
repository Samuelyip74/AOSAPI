from consumer import AOSAPI, AOSConnection


try:
    api = AOSAPI(AOSConnection(
    username = 'admin',
    password = 'switch123',
    hostaddress = '192.168.2.254',
    secure = True,
    obeyproxy = False,
    prettylinks = True,
    useport = 443,
    aosheaders = None,
    debug = False))
    api.login()
    results = api.query('cli', 'aos', {
    'cmd':'show+vlan'})['result']
    if api.success():
        results['data']['rows']
    else:
        pass
   
except:
    print ("Error: ")
    api.logout()
