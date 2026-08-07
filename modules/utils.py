from rich.console import Console
from rich.table import Table

console = Console()


def display_ping_results(stats):

    table = Table(title="PING TEST RESULTS")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Status", stats["status"])
    table.add_row("Packets Sent", str(stats["sent"]))
    table.add_row("Packets Received", str(stats["received"]))
    table.add_row("Packet Loss", stats["loss"])
    table.add_row("Minimum RTT", stats["min"] + " ms")
    table.add_row("Average RTT", stats["avg"] + " ms")
    table.add_row("Maximum RTT", stats["max"] + " ms")

    console.print(table)