# LoadX

DisLode is a lightweight Python load balancer distributing requests across backend servers using Round Robin.

## Features

- 🔄 **Round Robin**: Evenly distributes traffic.
- 🚀 **Concurrent**: Handles multiple clients via threading.
- 🛠️ **Customizable**: Easy backend configuration.
- 📜 **Lightweight**: Standard Python, no extra dependencies.

## How It Works

Client requests are received and routed to backend servers, which respond with HTTP messages. DisLode forwards these responses back to the client.

## Getting Started

### Prerequisites
- Python 3.8+

### Installation

```
git clone https://github.com/avaibh/LoadX.git & cd LoadX
```

### Testing
```
make all \
make test
```

---

## Usage

### 1. Start Backend Servers
Run multiple backend servers on different ports:
```python
python servers.py 9001 & python servers.py 9002 & python servers.py 9003 &
```

### 2. Start the Load Balancer
Run the load balancer:
```python
python lb.py
```

### 3. Test the Setup
Send requests to the load balancer:
```
curl http://127.0.0.1:8080 \
curl http://127.0.0.1:8080 \
curl http://127.0.0.1:8080
```


---

## Makefile Commands

| Command                  | Description                           |
| ------------------------ | ------------------------------------- |
| `make all`               | Start both load balancer and backends |
| `make run_load_balancer` | Start only the load balancer          |
| `make run_backends`      | Start all backend servers             |
| `make test`              | Test with curl                        |
| `make clean`             | Stop all running processes            |

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
