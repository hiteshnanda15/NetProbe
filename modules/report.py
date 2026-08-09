from pathlib import Path
import shutil


def export_report(diagnosis):
    """
    Export the latest network diagnosis.

    Reports are stored as:

        reports/
            <target>/
                report.txt

    If a report already exists for the same target,
    the old target folder is deleted and recreated.
    """

    # Main reports directory
    reports_dir = Path("reports")

    # Create reports directory if it doesn't exist
    reports_dir.mkdir(exist_ok=True)

    # Get hostname
    hostname = diagnosis["hostname"]

    # Make hostname safe for use as a folder name
    safe_hostname = (
        hostname
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
        .replace("?", "_")
        .replace("*", "_")
        .replace('"', "_")
        .replace("<", "_")
        .replace(">", "_")
        .replace("|", "_")
    )

    # Target-specific folder
    target_dir = reports_dir / safe_hostname

    # Delete previous report for this target
    if target_dir.exists():
        shutil.rmtree(target_dir)

    # Create fresh target folder
    target_dir.mkdir(parents=True)

    # Final report path
    report_file = target_dir / "report.txt"

    with open(report_file, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("                 NETPROBE REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(
            f"Generated At : {diagnosis['timestamp']}\n"
        )

        file.write(
            f"Target       : {diagnosis['hostname']}\n\n"
        )

        # ------------------------
        # DNS
        # ------------------------

        file.write("[1] DNS LOOKUP\n")
        file.write("-" * 40 + "\n")

        file.write(
            f"Status     : {diagnosis['dns_status']}\n"
        )

        file.write(
            f"IP Address : {diagnosis['ip']}\n"
        )

        file.write("\n")

        # ------------------------
        # PING
        # ------------------------

        file.write("[2] PING TEST\n")
        file.write("-" * 40 + "\n")

        ping = diagnosis["ping"]

        file.write(
            f"Status           : {ping['status']}\n"
        )

        file.write(
            f"Packets Sent     : {ping['sent']}\n"
        )

        file.write(
            f"Packets Received : {ping['received']}\n"
        )

        file.write(
            f"Packet Loss      : {ping['loss']}\n"
        )

        file.write(
            f"Minimum RTT      : {ping['min']} ms\n"
        )

        file.write(
            f"Average RTT      : {ping['avg']} ms\n"
        )

        file.write(
            f"Maximum RTT      : {ping['max']} ms\n"
        )

        file.write("\n")

        # ------------------------
        # HTTP
        # ------------------------

        file.write("[3] HTTP HEALTH CHECK\n")
        file.write("-" * 40 + "\n")

        http = diagnosis["http"]

        file.write(
            f"Target          : {http['url']}\n"
        )

        file.write(
            f"Status          : {http['status']}\n"
        )

        file.write(
            f"HTTP Status     : {http['http_status']}\n"
        )

        if http["response_time"] is not None:

            file.write(
                f"Response Time   : "
                f"{http['response_time']} ms\n"
            )

        else:

            file.write(
                "Response Time   : N/A\n"
            )

        if http["error"]:

            file.write(
                f"Error           : {http['error']}\n"
            )

        file.write("\n")

        # ------------------------
        # PORT SCAN
        # ------------------------

        file.write("[4] TCP PORT SCAN\n")
        file.write("-" * 40 + "\n")

        for result in diagnosis["ports"]:

            file.write(
                f"{result['port']:<8}"
                f"{result['service']:<15}"
                f"{result['status']}\n"
            )

        file.write("\n")

        # ------------------------
        # TRACEROUTE
        # ------------------------

        file.write("[5] TRACEROUTE\n")
        file.write("-" * 40 + "\n")

        file.write(
            diagnosis["traceroute"]["output"]
        )

        file.write("\n\n")

        # ------------------------
        # SUMMARY
        # ------------------------

        file.write("=" * 60 + "\n")
        file.write("                 DIAGNOSIS SUMMARY\n")
        file.write("=" * 60 + "\n\n")

        file.write(
            f"DNS         : {diagnosis['dns_status']}\n"
        )

        file.write(
            f"PING        : {diagnosis['ping_status']}\n"
        )

        file.write(
            f"HTTP        : {diagnosis['http_status']}\n"
        )

        file.write(
            f"PORT SCAN   : {diagnosis['port_status']}\n"
        )

        file.write(
            f"TRACEROUTE  : "
            f"{diagnosis['traceroute_status']}\n"
        )

        file.write("\n")

        file.write(
            f"Overall Status : "
            f"{diagnosis['overall_status']}\n"
        )

    return str(report_file)