from rich.console import Console

console = Console()


def show_menu():

    console.print("\n[bold yellow]Select an option:[/bold yellow]")

    console.print("1. DNS Lookup")
    console.print("2. Ping Test")
    console.print("3. HTTP Health Check")
    console.print("4. TCP Port Scan")
    console.print("5. Traceroute")
    console.print("6. Complete Network Diagnosis")
    console.print("7. Export Report")
    console.print("8. Exit")

    choice = input("\nEnter choice: ")

    return choice