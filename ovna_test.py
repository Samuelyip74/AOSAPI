import pysyslogclient

client = pysyslogclient.SyslogClientRFC5424("192.168.14.44", "10514", proto="UDP")

client.log("DESKTOP-MGFHUAM login, ips, botnet, attack",
	facility=pysyslogclient.FAC_SYSTEM,
	severity=pysyslogclient.SEV_EMERGENCY,
	program="Logger",
	pid=1,
	octet=pysyslogclient.OCTET_COUNTING)


# client = pysyslogclient.SyslogClientRFC5424("192.168.14.44", "514", proto="UDP")

# client.log("app=NwkAdvisor_Quarantine, src=192.168.11.40",
# 	facility=pysyslogclient.FAC_SYSTEM,
# 	severity=pysyslogclient.SEV_EMERGENCY,
# 	program="Logger",
# 	pid=1,
# 	octet=pysyslogclient.OCTET_COUNTING)



