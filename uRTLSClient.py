
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 



print("Sending...")
tag_rpt              = bytes.fromhex('0012fcc30200001c9c1c12ce8f0600009c1c1268f062c40a00109c1c1268f0600010001001ff06ff0000AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
station_rpt          = bytes.fromhex('0013fcc30200001c9c1c12ce8f0600009c1c1268f0625d0a06c402019c1c1268f0609c1c1268f06200000001AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
compound_msg         = bytes.fromhex("0014fcc50100005c9c1c12ce8f060000000200000013fcc30200001c9c1c12ce8f0600009c1c1268f0625d0a06c402019c1c1268f0609c1c1268f062000000010013fcc40200001c9c1c12ce8f060000085700190c5f5d0006d901019c1c1268f0609c1c1268f06400000001ebdee8abce05d6f25aea9a2ce8ea5ef81162c038")
compound_msg         = bytes.fromhex("0014fcc50100005c9c1c12ce8f060000000300000012fcc30200001c9c1c12ce8f0600009c1c1268f062c40a001001019c1c1268f0600000000001ff06ff00000013fcc30200001c9c1c12ce8f0600009c1c1268f0625d0a06c402019c1c1268f0609c1c1268f062000000010012fcc30200001c9c1c12ce8f0600009c1c1268f062c40a001001019c1c1268f0600000000001ff06ff0000ebdee8abce05d6f25aea9a2ce8ea5ef81162c038")
ap_notificaiton      = bytes.fromhex('0015fcc30200001c9c1c12ce8f0600009c1c1268f062c40a00109c1c1268f0600010001001ff06ff0000AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

#bytesToSend         = station_rpt
#bytesToSend         = tag_rpt
bytesToSend         = compound_msg
#bytesToSend         = ap_notificaiton

# serverAddressPort   = (IPAddr, 5000)
serverAddressPort   = ('127.0.0.1', 5000)
bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# msgFromServer = UDPClientSocket.recvfrom(bufferSize)
# msg = "Message from Server {}".format(msgFromServer[0])
# print(msg)
print("Sent")
