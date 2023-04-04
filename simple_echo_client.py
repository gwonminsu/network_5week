import socket
import argparse
host = 'localhost'

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to %s port %s" %server_address)
    sock.connect(server_address)

    try:
        message = "Test message. This message will be echoed."
        print(f"Sending {message}")
        sock.sendall(message.encode())
        amount_recieved = 0
        amount_expected = len(message)
        while amount_recieved < amount_expected:
            data = sock.recv(16)
            amount_recieved += len(data)
            print(f"Recieved: {len(data)} bytes [{data.decode()}]")
    except socket.errno as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Other exception: {str(e)}")
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)