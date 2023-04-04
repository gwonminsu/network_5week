import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Socket Error Exs')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    print(f"host : {host}, port : {port}, file : {filename}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket: [e]")
        sys.exit(1)

    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address-related error connection to server: {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error : {e}')
        sys.exit(1)

    try:
        message = f"GET /index.php HTTP/1.0\r\n\r\n"
        print(message)
        s.sendall(message.encode())
    except socket.error as e:
        print(f'Error sending data : {e}')
        sys.exit(1)

    while 1:

        try:
            buf = s.recv(2048)
            sys.stdout.write(buf.decode())
        except UnicodeEncodeError:
            bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout.buffer.write(bytes)
            else:
                text = bytes.decode(sys.stdout.encoding, 'strict')
                sys.stdout.write(text)
        except socket.error as e:
            print(f'Error receiving data: {e}')
            sys.exit(1)
        if not len(buf):
            break

if __name__ == '__main__':
    main()