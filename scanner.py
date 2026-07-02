import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Common service names for a nicer results string — extend as you like
COMMON_PORTS = {
    21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
    80: "http", 110: "pop3", 143: "imap", 443: "https",
    3306: "mysql", 3389: "rdp", 5432: "postgres", 8080: "http-alt",
}


def resolve_host(target):
    """Turn a hostname into an IP address (raises socket.gaierror if invalid)."""
    return socket.gethostbyname(target)


def _check_tcp_port(ip, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))
        return port if result == 0 else None


def _check_udp_port(ip, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(timeout)
        try:
            s.sendto(b"", (ip, port))
            s.recvfrom(1024)
            return port  # got a reply -> definitely open
        except socket.timeout:
            return port  # no response -> probably open or filtered
        except (ConnectionResetError, OSError):
            return None  # ICMP unreachable -> closed


def scan_ports(target, port_start, port_end, mode="tcp", timeout=1.0, max_threads=100):
    """
    Scan `target` from port_start to port_end (inclusive) using the given mode
    ('tcp', 'udp', or 'full'). Returns (ip_address, sorted_list_of_open_ports).
    """
    ip = resolve_host(target)
    ports = range(port_start, port_end + 1)
    open_ports = set()

    jobs = []
    if mode in ("tcp", "full"):
        jobs.append(("tcp", _check_tcp_port))
    if mode in ("udp", "full"):
        jobs.append(("udp", _check_udp_port))

    for _, check_fn in jobs:
        with ThreadPoolExecutor(max_workers=max_threads) as pool:
            futures = {pool.submit(check_fn, ip, p, timeout): p for p in ports}
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    open_ports.add(result)

    return ip, sorted(open_ports)


def format_ports(open_ports):
    """Turn [22, 80, 443] into 'ssh(22), http(80), https(443)' for display/storage."""
    if not open_ports:
        return ""
    return ", ".join(
        f"{COMMON_PORTS.get(p, '?')}({p})" for p in open_ports
    )