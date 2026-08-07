from modules.banner import show_banner
from modules.menu import show_menu
from modules.dns_lookup import dns_lookup
from modules.ping_test import ping_host
from modules.utils import display_ping_results


def main():

    show_banner()

    hostname = input("\nEnter Target Host (Example: google.com): ")

    while True:

        choice = show_menu()

        # ------------------------
        # Option 1
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
        # Option 2
        # ------------------------

        elif choice == "2":

            ping_stats = ping_host(hostname)

            display_ping_results(ping_stats)

        # ------------------------
        # Exit
        # ------------------------

        elif choice == "8":

            print("\nThank you for using NetProbe!")
            break

        else:

            print("\nInvalid Choice. Try Again.")


if __name__ == "__main__":
    main()