# Define variables for ports and backend servers
BACKEND_PORTS = 9001 9002 9003
PYTHON = python

# Default target: Run everything
all: run_load_balancer run_backends

# Target to run the load balancer
run_load_balancer:
	@echo "Starting Load Balancer..."
	$(PYTHON) lb.py &

# Target to run all backend servers
run_backends:
	@echo "Starting Backend Servers..."
	@for port in $(BACKEND_PORTS); do \
		echo "Starting backend server on port $$port..."; \
		$(PYTHON) servers.py $$port & \
	done

# Target to test the setup using curl
test:
	@echo "Testing Load Balancer..."
	@curl -s http://127.0.0.1:8080 || echo "Load Balancer not running!"
	@curl -s http://127.0.0.1:8080 || echo "Load Balancer not running!"
	@curl -s http://127.0.0.1:8080 || echo "Load Balancer not running!"

# Clean up background processes (Linux/Unix)
clean:
	@echo "Stopping all Python processes..."
	pkill -f lb.py || echo "No Load Balancer running."
	pkill -f servers.py || echo "No Backend Servers running."

# Help target to display available commands
help:
	@echo "Available commands:"
	@echo "  make all              - Start the load balancer and backend servers"
	@echo "  make run_load_balancer - Start the load balancer only"
	@echo "  make run_backends     - Start all backend servers"
	@echo "  make test             - Test the setup using curl"
	@echo "  make clean            - Stop all running Python processes"
