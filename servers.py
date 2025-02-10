# List of backend servers (IP, Port)
BACKEND_SERVERS = [
    ("127.0.0.1", 9001),  # Backend server 1
    ("127.0.0.1", 9002),  # Backend server 2
    ("127.0.0.1", 9003),  # Backend server 3
]

import socket
import sys

def start_backend_server(host='127.0.0.1', port=9001):
    """Start a simple backend HTTP server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen()
        print(f"Backend server listening on {host}:{port}...")
        
        while True:
            conn, addr = server.accept()
            with conn:
                print(f"Connected to client {addr}")
                data = conn.recv(1024)
                print(f"Received request:\n{data.decode()}")

                # Respond with a unique message for each backend
                response_body = f"Hello from Backend {port}!\n"
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "Content-Type: text/plain\r\n"
                    "\r\n"
                    f"{response_body}"
                )
                conn.sendall(response.encode())
                print("Response sent.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backend_server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_backend_server(port=port)
