import re

string = 'date=2023-03-27 time=14:36:58 logid="0100032002" type="event" subtype="system" level="alert" vd="root" eventtime=1679899018 logdesc="Admin login failed" sn="0" user="admin" ui="https(192.168.14.33)" method="https" srcip=192.168.14.33 dstip=10.100.100.254 action="login" status="failed" reason="passwd_invalid" msg="Administrator admin login failed from https(192.168.14.33) because of invalid password"'
logid, user, srcip, dstip, msg = re.findall(r'logid=\"(.*?)\" .*user=\"(.*?)\" .*srcip=(.*?)\ .*dstip=(.*?)\ .*msg=\"(.*?)\"',string)[0]
print(logid, user, srcip, dstip, msg)