import logging
import logging.handlers
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = ('192.168.28.28',10514))
my_logger.addHandler(handler)
my_logger.debug('DESKTOP-MGFHUAM date=2023-03-27 time=14:36:58 logid="0100032002" type="event" subtype="system" level="alert" vd="root" eventtime=1679899018 logdesc="Admin login failed" sn="0" user="admin" ui="https(192.168.14.33)" method="https" srcip=192.168.14.33 dstip=10.100.100.254 action="login" status="failed" reason="passwd_invalid" msg="Administrator admin login failed from https(192.168.14.33) because of invalid password"')
#my_logger.debug('DESKTOP-MGFHUAM logid="0100032002" ips spam srcip=192.168.14.33 dstip=10.100.100.254 action="login"')
