
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

#00010002000300040005000600070008

#msgFromClient       = bytes.fromhex('0015001002000010AABBCCDDEEFF0000111111111111111122222222222222AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#msgFromClient       = bytes.fromhex('0013001002000010AABBCCDDEEFF000000010002000300040005000600070008000100020003000400050006AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
msgFromClient       = bytes.fromhex("0014fcc50100005c9c1c12ce8f060000000200000013fcc30200001c9c1c12ce8f0600009c1c1268f0625d0a06c402019c1c1268f0609c1c1268f062000000010013fcc40200001c9c1c12ce8f060000085700190c5f5d0006d901019c1c1268f0609c1c1268f06400000001ebdee8abce05d6f25aea9a2ce8ea5ef81162c038")

bytesToSend         = msgFromClient

serverAddressPort   = (IPAddr, 5000)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

# msg = "Message from Server {}".format(msgFromServer[0])

# print(msg)