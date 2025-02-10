import socket
import threading
from route import Router
from servers import BACKEND_SERVERS

def handle_client(conn, addr):
    """Handle an individual client connection."""
    print(f"Connected to {addr}")

    # Receive data from the client
    client_data = conn.recv(1024)  
    print(f"Received: {client_data.decode()}")

    # Forward the client's request to the backend
    response = router.forward_request_to_backend(client_data)  

    # Send the response back to the client
    conn.sendall(response)
    conn.close()  # Close the connection
    print(f"Connection to {addr} closed")

def start_load_balancer(host='127.0.0.1', port=8080):
    """Start the load balancer."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Listening on {host}:{port}...")
        
        while True:
            conn, addr = server.accept()  # Accept a new client connection
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()  # Start a new thread to handle the client

if __name__ == "__main__":
    router = Router(BACKEND_SERVERS)
    start_load_balancer()