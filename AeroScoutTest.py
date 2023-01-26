
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
# -	Code : 0xD0
# -	Subcode : 0
# -	Length : 8
# -	Payload : MAC@ of AP + @ Bytes set to 0

Code = "D0"
Subcode = "01"
Length = "18"                   # Length of Payload
# 34:e7:0b:03:d1:60
mac = "34e70b03d160"            # 6 bytes - MAC of AP
#mac = "ffffffffffff"            # 6 bytes - MAC of AP
reserved_1 = "00000000000000000000" # 10 bytes reserved
dilution_factor = "00000032"    # 4 bytes - 50 measurements
timeout = "0005"                # 2 bytes - 5 seconds
reserved_2 = "0000"
payload = mac+reserved_1+dilution_factor+timeout+reserved_2

print("Sending...")
set_client_mode_start      = bytes.fromhex(Code+Subcode+Length+payload)
bytesToSend         = set_client_mode_start

# serverAddressPort   = (IPAddr, 5000)
# serverAddressPort   = ('127.0.0.1', 5000)
serverAddressPort   = ('192.168.13.1', 1144)

bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
# msg = "Message from Server {}".format(msgFromServer[0])
# #print(msg)
print("Sent")

