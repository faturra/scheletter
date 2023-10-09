import socket
from .config import server_address


def check_telnet_connection(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            return "1"
    except (socket.timeout, ConnectionRefusedError):
        return "0"

dapodik_connection_status = check_telnet_connection('api.smpn162jakarta.sch.id', 1162)
