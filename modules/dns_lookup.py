import socket


def dns_lookup(hostname):
    """
    Resolve a hostname into an IPv4 address.

    Parameters:
        hostname (str): Domain name entered by the user.

    Returns:
        str | None:
            Returns the IP address if successful.
            Returns None if the hostname cannot be resolved.
    """

    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    except socket.gaierror:
        return None