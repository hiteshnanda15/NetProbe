from modules.banner import show_banner
from modules.menu import show_menu
from modules.dns_lookup import dns_lookup
from modules.ping_test import ping_host
from modules.utils import display_ping_results
from modules.http_check import check_http


def main():

    show_banner()

    hostname = input("\nEnter Target Host (Example: google.com): ")

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

            # Add https automatically if the user
            # enters only a hostname.
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
                print(f"Error           : {result['error']}")

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