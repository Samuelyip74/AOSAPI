
# https://github.com/lukaskaplan/aruba-rtls

import socket
import sys
import hmac
from time import sleep

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
    field.append(payload[0:6])      #1
    field.append(payload[6:7])      #2
    field.append(payload[7:8])      #3
    field.append(payload[8:9])      #4
    field.append(payload[9:10])     #5
    field.append(payload[10:11])    #6
    field.append(payload[11:12])    #7
    field.append(payload[12:18])    #8
    field.append(payload[18:24])    #9
    field.append(payload[24:28])    #10
    return field;    

def parse_station_ex_report(payload):
    #
    # $payload = 56 byte binary ar_station_report message
    # Return array:
    # [0] = 6 byte - station MAC (ap or client)
    # [1] = 6 byte - BSSID
    # [2] = 33 byte - ESSID
    # [3] = 1 byte - Channel
    # [4] = 1 byte - Phy_type
    # [5] = 1 byte - RSSI
    # [6] = 2 byte - Duration
    # [7] = 2 byte - Num_packets
    # [8] = 1 byte - Noise_floor
    # [9] = 1 byte - Classification
    # [10] = 2 byte - Reserved

    field = []
    field.append(payload[0:6])      #0
    field.append(payload[6:12])     #1
    field.append(payload[12:45])    #2
    field.append(payload[45:46])    #3
    field.append(payload[46:47])    #4
    field.append(payload[47:48])    #5
    field.append(payload[48:50])    #6
    field.append(payload[50:52])    #7
    field.append(payload[52:53])    #8
    field.append(payload[53:54])    #9
    field.append(payload[54:56])    #10
    return field;    

def parse_ap_ex_report(payload):
    #
    # $payload = 52 byte binary ar_station_report message
    # Return array:
    # [0] = 6 byte - BSSID
    # [1] = 33 byte - ESSID
    # [2] = 1 byte - Channel
    # [3] = 1 byte - Phy_type
    # [4] = 1 byte - RSSI
    # [5] = 2 byte - Duration
    # [6] = 2 byte - Num_packets
    # [7] = 1 byte - Noise_floor
    # [8] = 1 byte - Classification
    # [9] = 1 byte - Match_type
    # [10] = 1 byte - Match_method
    # [11] = 2 byte - Reserved

    field = []
    field.append(payload[0:6])      #0
    field.append(payload[6:39])     #1
    field.append(payload[39:40])    #2
    field.append(payload[40:41])    #3
    field.append(payload[41:42])    #4
    field.append(payload[42:44])    #5
    field.append(payload[44:46])    #6
    field.append(payload[46:47])    #7
    field.append(payload[47:48])    #8
    field.append(payload[48:49])    #9
    field.append(payload[49:50])    #10
    field.append(payload[50:52])    #11    
    return field;    

def parse_ap_tag_report(payload):
    #
    # $payload = 28 byte binary ar_station_report message
    # Return array:
    # [0] = 6 byte - BSSID
    # [1] = 1 byte - RSSI
    # [2] = 1 byte - Noise_floor
    # [3] = 4 byte - Timestamp
    # [4] = 6 byte - Tag_mac
    # [5] = 2 byte - Frame_control
    # [6] = 2 byte - Sequence
    # [7] = 1 byte - Data rate
    # [8] = 1 byte - Tx_power
    # [9] = 1 byte - Channel
    # [10] = 1 byte - Battery
    # [11] = 2 byte - Reserved

    field = []
    field.append(payload[0:6])      #0
    field.append(payload[6:7])      #1
    field.append(payload[7:8])      #2
    field.append(payload[8:12])     #3
    field.append(payload[12:18])    #4
    field.append(payload[18:20])    #5
    field.append(payload[20:22])    #6
    field.append(payload[22:23])    #7
    field.append(payload[23:24])    #8
    field.append(payload[24:25])    #9
    field.append(payload[25:26])    #10
    field.append(payload[26:28])    #11    
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
while(True):
    try:
        
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        APIPaddress = bytesAddressPair[1]
        message = rcv_explode(bytesAddressPair[0])

        if check_signature(message):            

            message_type = get_msg_type(message[0])

            if(message_type == "AR_AP_NOTIFICATION"):
                #
                # If we receive AR_AP_NOTIFICATION,
                # we have to acknowledge it.
                #                
                # print ("Received AR_AP_NOTIFICATION")
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
                # print ("Sent AR_AP_ACKNOWLEDGEMENT")
                            
            # 
            # If we receive AR_COMPOUND_MESSAGE_REPORT.
            # we have to parse it to submessages,
            # and then extract data and save them to database.
            #
            if(message_type == "AR_COMPOUND_MESSAGE_REPORT"):
                msg_count = int(message[1][0:2].hex())
                print("AR_COMPOUND_MESSAGE_REPORT")
                offset = 0
                for i in range(msg_count):
                    payload = message[1][4 + offset:]
                    msg_type = get_msg_type(payload[0:2])
                    if(msg_type == "AR_STATION_REPORT"):
                        print("AR_STATION_REPORT")
                        size = 44
                        sub_msg = message[1][4 + offset: 4 + offset + size]
                        station_rpt = parse_stationreport(sub_msg[16:])
                        station_rpt_json = {
                            "ap_mac"        : station_rpt[0].hex(),
                            "noise_floor"   : station_rpt[1].hex(),
                            "data_rate"     : station_rpt[2].hex(),
                            "channel"       : station_rpt[3].hex(),
                            "rssi"          : station_rpt[4].hex(),
                            "type"          : station_rpt[5].hex(),
                            "associated"    : station_rpt[6].hex(),
                            "radio_bssid"   : station_rpt[7].hex(),   
                            "mon_bssid"     : station_rpt[8].hex(), 
                            "age"           : station_rpt[9].hex(),   
                        }
                        print(station_rpt_json)
                    if(msg_type == "AR_STATION_EX_REPORT"):
                        print("AR_STATION_EX_REPORT")
                        size = 56
                        sub_msg = message[1][4 + offset: 4 + offset + size]
                        station_rpt = parse_station_ex_report(sub_msg[16:])
                        station_rpt_json = {
                            "ap_mac"        : station_rpt[0].hex(),
                            "BSSID"         : station_rpt[1].hex(),
                            "ESSID"         : station_rpt[2].hex(),
                            "channel"       : station_rpt[3].hex(),
                            "Phy_type"      : station_rpt[4].hex(),
                            "RSSI"          : station_rpt[5].hex(),
                            "Duration"      : station_rpt[6].hex(),
                            "Num_packets"   : station_rpt[7].hex(),   
                            "Noise_floor"   : station_rpt[8].hex(), 
                            "Classification": station_rpt[9].hex(),  
                            "Reserved"      : station_rpt[10].hex(),    
                        }
                        print(station_rpt_json) 
                    if(msg_type == "AR_AP_EX_REPORT"):
                        print("AR_AP_EX_REPORT")                       
                        size = 52
                        sub_msg = message[1][4 + offset: 4 + offset + size]
                        station_rpt = parse_ap_ex_report(sub_msg[16:])
                        station_rpt_json = {
                            "BSSID"         : station_rpt[0].hex(),
                            "ESSID"         : station_rpt[1].hex(),
                            "Channel"       : station_rpt[2].hex(),
                            "Phy_type"      : station_rpt[3].hex(),
                            "RSSI"          : station_rpt[4].hex(),
                            "Duration"      : station_rpt[5].hex(),
                            "Num_packets"   : station_rpt[6].hex(),
                            "Noise_floor"   : station_rpt[7].hex(),   
                            "Classification": station_rpt[8].hex(), 
                            "Match_type"    : station_rpt[9].hex(),  
                            "Match_method"  : station_rpt[10].hex(),  
                            "Reserved"      : station_rpt[11].hex(),   
                        }
                        print(station_rpt_json)  
                    if(msg_type == "AR_TAG_REPORT"):
                        print("AR_TAG_REPORT")                       
                        size = 44
                        sub_msg = message[1][4 + offset: 4 + offset + size]
                        station_rpt = parse_ap_tag_report(sub_msg[16:])
                        station_rpt_json = {
                            "BSSID"         : station_rpt[0].hex(),
                            "RSSI"          : station_rpt[1].hex(),
                            "Noise_floor"   : station_rpt[2].hex(),
                            "Timestamp"     : station_rpt[3].hex(),
                            "Tag_mac"       : station_rpt[4].hex(),
                            "Frame_control" : station_rpt[5].hex(),
                            "Sequence"      : station_rpt[6].hex(),
                            "Data rate"     : station_rpt[7].hex(),   
                            "Tx_power"      : station_rpt[8].hex(), 
                            "Channel"       : station_rpt[9].hex(),  
                            "Battery"       : station_rpt[10].hex(),  
                            "Reserved"      : station_rpt[11].hex(),   
                        }
                        print(station_rpt_json)                                                                       
                    offset += size

            if(message_type == "AR_STATION_REPORT"):
                # print ("Received AR_STATION_REPORT")
                station_rpt = parse_stationreport(message[1])
                station_rpt_json = {
                    "ap_mac"        : station_rpt[0].hex(),
                    "noise_floor"   : station_rpt[1].hex(),
                    "data_rate"     : station_rpt[2].hex(),
                    "channel"       : station_rpt[3].hex(),
                    "rssi"          : station_rpt[4].hex(),
                    "type"          : station_rpt[5].hex(),
                    "associated"    : station_rpt[6].hex(),
                    "radio_bssid"   : station_rpt[7].hex(),   
                    "mon_bssid"     : station_rpt[8].hex(), 
                    "age"           : station_rpt[9].hex(),   
                }
                print(station_rpt_json)                
                # print ("Sent AR_STATION_REPORT")      
        
            if(message_type == "AR_STATION_EX_REPORT"):
                #print ("Received AR_STATION_EX_REPORT")
                station_rpt = parse_station_ex_report(message[1])
                station_rpt_json = {
                    "ap_mac"        : station_rpt[0].hex(),
                    "BSSID"         : station_rpt[1].hex(),
                    "ESSID"         : station_rpt[2].hex(),
                    "channel"       : station_rpt[3].hex(),
                    "Phy_type"      : station_rpt[4].hex(),
                    "RSSI"          : station_rpt[5].hex(),
                    "Duration"      : station_rpt[6].hex(),
                    "Num_packets"   : station_rpt[7].hex(),   
                    "Noise_floor"   : station_rpt[8].hex(), 
                    "Classification": station_rpt[9].hex(),  
                    "Reserved"      : station_rpt[10].hex(),  
                }
                print(station_rpt_json) 

        else:
            # DO NOTHING
            pass

    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')
        exit()

    