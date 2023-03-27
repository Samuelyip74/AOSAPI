import logging
import logging.handlers
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = ('192.168.28.31',10514))
my_logger.addHandler(handler)
my_logger.debug('DESKTOP-MGFHUAM logid="0100032002" botnet user="admin" srcip=192.168.14.33 dstip=10.100.100.254 action="login"')
