import socket

class Router:
    def __init__(self, backends):
        """Initialize the router with a list of backend servers."""
        self.backends = backends
        # Keeps track of the current backend index for round robin
        self.index = 0  

    def get_next_backend(self):
        """Get the next backend server using round-robin."""
        backend = self.backends[self.index]
        self.index = (self.index + 1) % len(self.backends)  # Move to the next backend
        return backend

    def forward_request_to_backend(self, client_data):
        """Forward the client's request to a backend server and return the response."""
        selected_backend = self.get_next_backend()
        print(f"Forwarding request to backend {selected_backend}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_conn:
            backend_conn.connect(selected_backend)
            backend_conn.sendall(client_data)

            # Receive response from the backend
            response = b""
            while True:
                chunk = backend_conn.recv(1024)
                if not chunk:
                    break
                response += chunk

            return response
