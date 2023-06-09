import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.1.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print(f"IP address: {ip_addr} =>" 
              f"Packed: {hexlify(packed_ip_addr)}, "
              f"Unpacked: {unpacked_ip_addr}")

if __name__ == '__main__':
    convert_ip4_address()