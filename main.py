from modules.banner import show_banner
from modules.menu import show_menu
from modules.dns_lookup import dns_lookup
from modules.ping_test import ping_host
from modules.utils import display_ping_results
from modules.http_check import check_http
from modules.port_scan import scan_common_ports
from modules.traceroute_test import run_traceroute


def main():

    show_banner()

    hostname = input(
        "\nEnter Target Host (Example: google.com): "
    ).strip()

    while True:

        choice = show_menu()

        # ------------------------
        # Option 1 - DNS Lookup
        # ------------------------

        if choice == "1":

            ip = dns_lookup(hostname)

            if ip:

                print("\nDNS LOOKUP")
                print("----------------------------")
                print(f"Hostname : {hostname}")
                print(f"IP Address : {ip}")

            else:

                print("\nDNS Resolution Failed")

        # ------------------------
        # Option 2 - Ping Test
        # ------------------------

        elif choice == "2":

            ping_stats = ping_host(hostname)

            display_ping_results(ping_stats)

        # ------------------------
        # Option 3 - HTTP Health Check
        # ------------------------

        elif choice == "3":

            print("\nHTTP HEALTH CHECK")
            print("----------------------------")

            url = input(
                "Enter URL (Example: https://google.com): "
            ).strip()

            if not url.startswith(("http://", "https://")):
                url = "https://" + url

            result = check_http(url)

            print(f"\nTarget          : {url}")
            print(f"Status          : {result['status']}")
            print(f"HTTP Status     : {result['http_status']}")

            if result["response_time"] is not None:

                print(
                    f"Response Time   : "
                    f"{result['response_time']} ms"
                )

            else:

                print("Response Time   : N/A")

            if result["status"] == "DOWN":

                print(
                    f"Error           : "
                    f"{result['error']}"
                )

        # ------------------------
        # Option 4 - TCP Port Scan
        # ------------------------

        elif choice == "4":

            print("\nTCP PORT SCAN")
            print("----------------------------")

            results = scan_common_ports(hostname)

            print(f"Target : {hostname}\n")

            print(
                f"{'Port':<8}"
                f"{'Service':<15}"
                f"Status"
            )

            print("-" * 35)

            for result in results:

                print(
                    f"{result['port']:<8}"
                    f"{result['service']:<15}"
                    f"{result['status']}"
                )

        # ------------------------
        # Option 5 - Traceroute
        # ------------------------

        elif choice == "5":

            print("\nTRACEROUTE")
            print("----------------------------")
            print(f"Target : {hostname}")

            result = run_traceroute(hostname)

            if result["status"] == "SUCCESS":

                print("\nTraceroute Results")
                print("----------------------------")
                print(result["output"])

            else:

                print("\nTraceroute Failed")
                print("----------------------------")
                print(result["output"])

        # ------------------------
        # Option 6 - Complete
        # Network Diagnosis
        # ------------------------

        elif choice == "6":

            print("\n")
            print("=" * 55)
            print("          COMPLETE NETWORK DIAGNOSIS")
            print("=" * 55)

            print(f"\nTarget : {hostname}")

            # ------------------------
            # DNS
            # ------------------------

            print("\n[1] DNS LOOKUP")
            print("----------------------------")

            ip = dns_lookup(hostname)

            if ip:

                dns_status = "PASS"

                print(f"Hostname  : {hostname}")
                print(f"IP Address: {ip}")

            else:

                dns_status = "FAIL"

                print("DNS Resolution Failed")

            # ------------------------
            # PING
            # ------------------------

            print("\n[2] PING TEST")
            print("----------------------------")

            ping_stats = ping_host(hostname)

            display_ping_results(ping_stats)

            if ping_stats["status"] == "REACHABLE":

                ping_status = "PASS"

            else:

                ping_status = "FAIL"

            # ------------------------
            # HTTP
            # ------------------------

            print("\n[3] HTTP HEALTH CHECK")
            print("----------------------------")

            url = f"https://{hostname}"

            http_result = check_http(url)

            print(f"Target          : {url}")
            print(f"Status          : {http_result['status']}")
            print(f"HTTP Status     : {http_result['http_status']}")

            if http_result["response_time"] is not None:

                print(
                    f"Response Time   : "
                    f"{http_result['response_time']} ms"
                )

            else:

                print("Response Time   : N/A")

            if http_result["status"] == "UP":

                http_status = "PASS"

            else:

                http_status = "FAIL"

                if http_result["error"]:
                    print(
                        f"Error           : "
                        f"{http_result['error']}"
                    )

            # ------------------------
            # PORT SCAN
            # ------------------------

            print("\n[4] TCP PORT SCAN")
            print("----------------------------")

            port_results = scan_common_ports(hostname)

            print(
                f"{'Port':<8}"
                f"{'Service':<15}"
                f"Status"
            )

            print("-" * 35)

            open_ports = 0

            for result in port_results:

                print(
                    f"{result['port']:<8}"
                    f"{result['service']:<15}"
                    f"{result['status']}"
                )

                if result["status"] == "OPEN":
                    open_ports += 1

            if open_ports > 0:

                port_status = "PASS"

            else:

                port_status = "WARNING"

            # ------------------------
            # TRACEROUTE
            # ------------------------

            print("\n[5] TRACEROUTE")
            print("----------------------------")

            traceroute_result = run_traceroute(hostname)

            if traceroute_result["status"] == "SUCCESS":

                traceroute_status = "PASS"

                print(traceroute_result["output"])

            else:

                traceroute_status = "FAIL"

                print(traceroute_result["output"])

            # ------------------------
            # FINAL SUMMARY
            # ------------------------

            print("\n")
            print("=" * 55)
            print("               DIAGNOSIS SUMMARY")
            print("=" * 55)

            print(f"\nDNS         : {dns_status}")
            print(f"PING        : {ping_status}")
            print(f"HTTP        : {http_status}")
            print(f"PORT SCAN   : {port_status}")
            print(f"TRACEROUTE  : {traceroute_status}")

            # Determine overall health

            if (
                dns_status == "PASS"
                and ping_status == "PASS"
                and http_status == "PASS"
                and traceroute_status == "PASS"
            ):

                overall_status = "HEALTHY"

            elif (
                dns_status == "FAIL"
                or ping_status == "FAIL"
            ):

                overall_status = "CRITICAL"

            else:

                overall_status = "DEGRADED"

            print("\n" + "-" * 55)
            print(f"Overall Status : {overall_status}")
            print("-" * 55)

        # ------------------------
        # Option 8 - Exit
        # ------------------------

        elif choice == "8":

            print("\nThank you for using NetProbe!")
            break

        # ------------------------
        # Invalid Option
        # ------------------------

        else:

            print("\nInvalid Choice. Try Again.")


if __name__ == "__main__":
    main()