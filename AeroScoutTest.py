
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
mac = "ffffffffffff"            # 6 bytes - MAC of AP
dilution_factor = "00000032"    # 4 bytes - 50 measurements
timeout = "0005"                # 2 bytes - 5 seconds
payload = mac+dilution_factor+timeout

print("Sending...")
set_client_mode_start      = bytes.fromhex(Code+Subcode+Length+payload)


bytesToSend         = set_client_mode_start

# serverAddressPort   = (IPAddr, 5000)
serverAddressPort   = ('127.0.0.1', 5000)
# serverAddressPort   = ('192.168.14.28', 5000)

bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
# msg = "Message from Server {}".format(msgFromServer[0])
# #print(msg)
print("Sent")

