import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(f'Starting up echo server on {host} port {port}')
    sock.bind((host, port))
    sock.listen(backlog)
    while True:
        print('Waiting to receive message from client')
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print(f'Data: {data.decode()}')
            client.send(data)
            print(f'sent {data.decode()} bytes back to {address}')
            client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)