import pysyslogclient

client = pysyslogclient.SyslogClientRFC5424("192.168.28.28", "10514", proto="UDP")

client.log("DESKTOP-MGFHUAM login, ips, botnet, attack",
	facility=pysyslogclient.FAC_SYSTEM,
	severity=pysyslogclient.SEV_EMERGENCY,
	program="Logger",
	pid=1,
	octet=pysyslogclient.OCTET_COUNTING)


