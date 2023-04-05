import logging
import logging.handlers
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = ('192.168.28.28',10514))
my_logger.addHandler(handler)
# Login failed
#my_logger.debug('date=2023-03-27 time=14:36:58 logid="0100032002" type="event" subtype="system" level="alert" vd="root" eventtime=1679899018 logdesc="Admin login failed" sn="0" user="admin" ui="https(192.168.14.33)" method="https" srcip=192.168.14.33 dstip=10.100.100.254 action="login" status="failed" reason="passwd_invalid" msg="Administrator admin login failed from https(192.168.14.33) because of invalid password"')
# IPS syslog
#my_logger.debug('logid="0419016384" type="utm" subtype="ips" attack="Eicar.Virus.Test.File" severity="info" srcip=172.16.200.55 srccountry="Reserved" dstip=10.1.100.11  ref="http://www.fortinet.com/ids/VID29844" user="bob" dstintfrole="undefined" sessionid=901 action="reset" proto=6 service="HTTP" policyid=1 srcport=80 dstport=44362 hostname="172.16.200.55" url="/virus/eicar.com" direction="incoming" attackid=29844 profile="test-ips" incidentserialno=877326946 msg="file_transfer: Eicar.Virus.Test.File,"')
my_logger.debug('date=2019-05-15 time=17:56:41 logid="0419016384" type="utm" subtype="ips" eventtype="signature" level="alert" vd="root" eventtime=1557968201 severity="critical" srcip=10.1.100.22 srccountry="Reserved" dstip=172.16.200.55 srcintf="port10" srcintfrole="lan" dstintf="port9" dstintfrole="wan" sessionid=4017 action="dropped" proto=6 service="HTTP" policyid=1 attack="Adobe.Flash.newfunction.Handling.Code.Execution" srcport=46810 dstport=80 hostname="172.16.200.55" url="/ips/sig1.pdf" direction="incoming" attackid=23305 profile="block-critical-ips" ref="http://www.fortinet.com/ids/VID23305" incidentserialno=582633933 msg="applications3: Adobe.Flash.newfunction.Handling.Code.Execution," crscore=50 craction=4096 crlevel="critical"')
#my_logger.debug('DESKTOP-MGFHUAM logid="0100032002" ips spam srcip=192.168.14.33 dstip=10.100.100.254 action="login"')
