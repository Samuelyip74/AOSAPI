
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

#00010002000300040005000600070008

#msgFromClient       = bytes.fromhex('0015001002000010AABBCCDDEEFF0000111111111111111122222222222222AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
msgFromClient       = bytes.fromhex('0013001002000010AABBCCDDEEFF000000010002000300040005000600070008000100020003000400050006AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

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