
import sys
import hmac

key_val = "abcxyz"

ack_header = bytes.fromhex("0010038301000000946424c31dda0000")
#ack_header = bytes.fromhex("0015038301000000946424c31dda0000")

ack_hmac = hmac.new(key=key_val.encode(), msg=ack_header, digestmod="sha1")
ack_checksum = ack_hmac.digest()
print(ack_checksum.hex())
