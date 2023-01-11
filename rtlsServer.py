
# https://github.com/lukaskaplan/aruba-rtls

import socket
import sys
import hmac

key_val = "abcxyz"

def get_msg_type(header):
    #
    # header = 16 byte binary RTLS header
    # return string - name/type of the message
    # 
    type = header[0:2]
    if(type == b"\x00\x00"): return "AR_AS_CONFIG_SET"
    if(type == b"\x00\x01"): return "AR_STATION_REQUEST"
    if(type == b"\x00\x10"): return "AR_ACK"
    if(type == b"\x00\x11"): return "AR_NACK"
    if(type == b"\x00\x12"): return "AR_TAG_REPORT"
    if(type == b"\x00\x13"): return "AR_STATION_REPORT"
    if(type == b"\x00\x14"): return "AR_COMPOUND_MESSAGE_REPORT"
    if(type == b'\x00\x15'): return "AR_AP_NOTIFICATION"
    if(type == b"\x00\x16"): return "AR_MMS_CONFIG_SET"
    if(type == b"\x00\x17"): return "AR_STATION_EX_REPORT"
    if(type == b"\x00\x18"): return "AR_AP_EX_REPORT"
    else: return "UNKNOWN"
    

def rcv_explode(message):
    #
    # $message = whole RTLS binary message
    # return array:
    # [0] = 16 byte - RTLS header
    # [1] = RTLS payload
    # [2] = 20 byte - RTLS hmac-sha1 hash of header and payload
    #
    rtls = [] 
    rtls.append(message[:16])
    rtls.append(message[16:-20])
    rtls.append(message[-20:])
    return rtls

def parse_header(header):
    #
    # $header = 16 byte header in binary
    # return array
    # [0] = 2 byte - Message type
    # [1] = 2 byte - Message Id
    # [2] = 1 byte - Major version (1 or 2)
    # [3] = 1 byte - Minor version (always 0)
    # [4] = 2 byte - Data Length (length of rtls payload)
    # [5] = 6 byte - AP MAC
    # [6] = 2 byte - Padding
    #
    field = []
    field.append(header[0:2])
    field.append(header[2:4])
    field.append(header[4:5])
    field.append(header[5:6])
    field.append(header[6:8])
    field.append(header[8:14])
    field.append(header[14:16])
    return field;    

def parse_stationreport(payload):
    #
    # $payload = 28 byte binary ar_station_report message
    # Return array:
    # [0] = 6 byte - station MAC (ap or client)
    # [1] = 1 byte - noise floor
    # [2] = 1 byte - Data rate
    # [3] = 1 byte - Channel
    # [4] = 1 byte - RSSI
    # [5] = 1 byte - Type (AR_WLAN_CLIENT, AR_WLAN_AP)
    # [6] = 1 byte - Associated (1= all aps and associated stations, 2= unassociated stations)
    # [7] = 6 byte - Radio_BSSID (radio which detected the device)
    # [8] = 6 byte - Mon_BSSID (AP that the station is associated to)
    # [9] = 4 byte - age, # of seconds since the last packet was heard from this station
    #
    field = []
    field.append(payload[0:6]) 
    field.append(payload[6:7]) 
    field.append(payload[7:8]) 
    field.append(payload[8:9]) 
    field.append(payload[9:10]) 
    field.append(payload[10:11]) 
    field.append(payload[11:12]) 
    field.append(payload[12:18]) 
    field.append(payload[18:24]) 
    field.append(payload[24:28]) 
    return field;    

def check_signature(message):
    return True

# local Server information
print("Starting RTLS Service ...")
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
localIP     = IPAddr
localPort   = 5000
bufferSize  = 1024

 
# Create a socket and bind to server
try:
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("Service started ...")
    print("RTLS server up and listening to data")
except socket.error as e:
    print ("\nError starting service: %s" % e)
    sys.exit(1)

# Listen for incoming datagrams
try:
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        APIPaddress = bytesAddressPair[1]
        message = rcv_explode(bytesAddressPair[0])

        if check_signature(message):            
            #
            # If we receive AR_AP_NOTIFICATION,
            # we have to acknowledge it.
            #
            message_type = get_msg_type(message[0])

            if(message_type == "AR_AP_NOTIFICATION"):
                print ("Received AR_AP_NOTIFICATION")
                # Change message type to acknowledgement
                header = parse_header(message[0])
                header[0] = bytes.fromhex('0010')

                # Implode header into bytes for sending
                ack_header = b''.join(header)

                # Generate hmac signature
                ack_hmac = hmac.new(key=key_val.encode(), msg=ack_header, digestmod="sha1")
                ack_checksum = ack_hmac.digest()

                # Create RTLS acknowledge packet, RTLS header + signature
                ack_msg = ack_header + ack_checksum[:20]

                # Send ack to AP
                UDPServerSocket.sendto(ack_msg, APIPaddress) 
                print ("Sent AR_AP_ACKNOWLEDGEMENT")

            
            # 
            # If we receive AR_COMPOUD_REPORT.
            # we have to parse it to submessages,
            # and then extract data and save them to database.
            #
            if(message_type == "AR_COMPOUND_MESSAGE_REPORT"):
                pass

            if(message_type == "AR_STATION_REPORT"):
                print ("Received AR_STATION_REPORT")
                msg = parse_stationreport(message[1])
                print ("Sent AR_STATION_REPORT")      
        
            #clientMsg = "Message from Client:{}".format(message)
            #clientIP  = "Client IP Address:{}".format(APIPaddress)
            
            # print(clientMsg)
            # print(clientIP)
    else:
        # DO NOTHING
        pass

except KeyboardInterrupt:
    print("KeyboardInterrupted")
    exit()

    