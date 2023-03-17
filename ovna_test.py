import pysyslogclient

client = pysyslogclient.SyslogClientRFC5424("192.168.28.24", "10514", proto="UDP")

client.log("DESKTOP-MGFHUAM hello Mar 14, 2023 4:27:30 pm[AUTH] :Login incorrect (eap_peap: TLS Alert read:fatal:unknown CA): [host/LPF2S7H80.corp.local] (from client radius port 2 cli C03C59293650)",
	facility=pysyslogclient.FAC_SYSTEM,
	severity=pysyslogclient.SEV_EMERGENCY,
	program="Logger",
	pid=1,
	octet=pysyslogclient.OCTET_COUNTING)



# import socket

 

# msgFromClient       = "DESKTOP-MGFHUAM Hello UDP Server"

# bytesToSend         = str.encode(msgFromClient)

# serverAddressPort   = ("192.168.28.24", 10514)

# bufferSize          = 1024

 

# # Create a UDP socket at client side

# UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# # Send to server using created UDP socket

# UDPClientSocket.sendto(bytesToSend, serverAddressPort)

