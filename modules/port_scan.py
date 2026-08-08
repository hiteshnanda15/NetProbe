import socket


COMMON_PORTS = {
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT"
}


def scan_port(host, port, timeout=1):

    try:

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(timeout)

            result = sock.connect_ex(
                (host, port)
            )

            if result == 0:
                return "OPEN"

            return "CLOSED"

    except socket.error:

        return "ERROR"


def scan_common_ports(host):

    results = []

    for port, service in COMMON_PORTS.items():

        status = scan_port(host, port)

        results.append({
            "port": port,
            "service": service,
            "status": status
        })

    return results