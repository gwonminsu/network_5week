import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode(), (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data:
        print(f"Response received from: {address}")
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        print(f'\tTime={time.ctime(t)}')

if __name__ == "__main__":
    sntp_client()