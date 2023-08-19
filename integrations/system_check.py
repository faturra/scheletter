import socket


def check_telnet_connection(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            return "1"
    except (socket.timeout, ConnectionRefusedError):
        return "0"

dapodik_connection_status = check_telnet_connection('127.0.0.1', 5774)
