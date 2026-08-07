import subprocess
import re


def ping_host(hostname):
    """
    Runs ping and returns parsed statistics.
    """

    try:
        result = subprocess.run(
            ["ping", "-c", "4", hostname],
            capture_output=True,
            text=True
        )

        output = result.stdout

        stats = {
            "sent": 0,
            "received": 0,
            "loss": "Unknown",
            "min": "N/A",
            "avg": "N/A",
            "max": "N/A",
            "status": "DOWN"
        }

        # Packet statistics
        packet_match = re.search(
            r"(\d+) packets transmitted, (\d+) packets received, ([\d.]+)% packet loss",
            output
        )

        if packet_match:
            stats["sent"] = int(packet_match.group(1))
            stats["received"] = int(packet_match.group(2))
            stats["loss"] = packet_match.group(3) + "%"

        # RTT statistics
        rtt_match = re.search(
            r"round-trip min/avg/max/stddev = ([\d.]+)/([\d.]+)/([\d.]+)/",
            output
        )

        if rtt_match:
            stats["min"] = rtt_match.group(1)
            stats["avg"] = rtt_match.group(2)
            stats["max"] = rtt_match.group(3)

        if stats["received"] > 0:
            stats["status"] = "REACHABLE"

        return stats

    except Exception as e:
        return {"error": str(e)}