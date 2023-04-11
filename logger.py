import logging
import logging.handlers
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = ('192.168.2.243',10514))
my_logger.addHandler(handler)
# Login failed
#my_logger.debug('date=2023-03-27 time=14:36:58 logid="0100032002" type="event" subtype="system" level="alert" vd="root" eventtime=1679899018 logdesc="Admin login failed" sn="0" user="admin" ui="https(192.168.14.33)" method="https" srcip=192.168.14.11 dstip=10.100.100.254 action="login" status="failed" reason="passwd_invalid" msg="Administrator admin login failed from https(192.168.14.33) because of invalid password"')

# IPS syslog
#my_logger.debug('logid="0419016384" type="utm" subtype="ips" attack="Eicar.Virus.Test.File" severity="info" srcip=172.16.200.55 srccountry="Reserved" dstip=10.1.100.11  ref="http://www.fortinet.com/ids/VID29844" user="bob" dstintfrole="undefined" sessionid=901 action="reset" proto=6 service="HTTP" policyid=1 srcport=80 dstport=44362 hostname="172.16.200.55" url="/virus/eicar.com" direction="incoming" attackid=29844 profile="test-ips" incidentserialno=877326946 msg="file_transfer: Eicar.Virus.Test.File,"')


# Email Filter
#my_logger.debug('date=2019-04-09 time=03:41:18 logid="0510020491" type="utm" subtype="emailfilter" eventtype="imap" level="notice" vd="vdom1" eventtime=1554806478647415130 policyid=1 sessionid=439 srcip=10.1.100.22 srcport=39937 srcintf="port21" srcintfrole="undefined" dstip=172.16.200.45 dstport=143 dstintf="port17" dstintfrole="undefined" proto=6 service="IMAPS" profile="822881" action="blocked" from="testpc3@qa.fortinet.com" to="testpc3@qa.fortinet.com" recipient="testpc3" direction="incoming" msg="from ip is in ip blocklist.(path block ip 172.16.200.9)" subject="testcase822881" size="525" attachment="no"')

# Anomaly
#my_logger.debug('date=2019-05-15 time=17:56:41 logid="0419016384" type="utm" subtype="anomaly" eventtype="signature" level="alert" vd="root" eventtime=1557968201 severity="critical" srcip=10.1.100.22 srccountry="Reserved" dstip=172.16.200.55 srcintf="port10" srcintfrole="lan" dstintf="port9" dstintfrole="wan" sessionid=4017 action="dropped" proto=6 service="HTTP" policyid=1 attack="Adobe.Flash.newfunction.Handling.Code.Execution" srcport=46810 dstport=80 hostname="172.16.200.55" url="/ips/sig1.pdf" direction="incoming" attackid=23305 profile="block-critical-ips" count=100 ref="http://www.fortinet.com/ids/VID23305" incidentserialno=582633933 msg="applications3: Adobe.Flash.newfunction.Handling.Code.Execution," crscore=50 craction=4096 crlevel="critical"')

# Webfilter
my_logger.debug('logid="0419016384" type="utm" subtype="webfilter" attack="Eicar.Virus.Test.File" severity="info" srcip=172.16.200.55 srccountry="Reserved" dstip=10.1.100.11  ref="http://www.fortinet.com/ids/VID29844" user="bob" dstintfrole="undefined" sessionid=901 action="reset" proto=6 service="HTTP" policyid=1 srcport=80 dstport=44362 hostname="172.16.200.55" url="/virus/eicar.com" direction="incoming" attackid=29844 profile="test" incidentserialno=877326946 msg="file_transfer: Eicar.Virus.Test.File,"')